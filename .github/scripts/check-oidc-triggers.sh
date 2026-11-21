#!/usr/bin/env bash
# Copy of linkt-ai/admin-infra scripts/ci/check-oidc-triggers.sh at 21b4fa3 (v1.0.0).
# This repository is public and cannot call the private admin-infra action.
# Update this copy when the admin-infra script changes.
# ADR-0010 trigger rule check (ADM-121, spec section 12).
#
# Usage: scripts/ci/check-oidc-triggers.sh <workflow-dir>
#
# A workflow that grants `id-token: write` (or `write-all`) must not declare a
# pull_request_target, workflow_run, issue_comment, issues, discussion or
# discussion_comment trigger. Those triggers run with the default branch ref,
# which a consumer OIDC role trusts, on input from an untrusted pull request,
# issue or comment.
#
# Each repository that calls .github/actions/credential or app-token runs this
# check in its own CI through .github/actions/oidc-trigger-check.
#
# The parser is the one in scripts/test/test_adm131_ci_broker_token_assertions.sh:
#   * A grant is `id-token: write` in block or flow style, with the key or the
#     value in quotes or not, or `write-all` anywhere.
#   * The `on:` section is read in each form: a scalar, a flow list, a flow
#     map, a block map and a block list. Only first level names count.
#
# Exit status: 0 when no workflow breaks the rule, 1 on a violation, 2 on a
# usage error or when the directory holds no *.yml or *.yaml file. A check of
# zero workflows proves nothing, so it never passes. It needs bash and python3
# (standard library only).
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <workflow-dir>" >&2
  exit 2
fi
dir="$1"
if [ ! -d "$dir" ]; then
  echo "check-oidc-triggers: '$dir' is not a directory" >&2
  exit 2
fi

checked=0
violations=0
while IFS= read -r wf; do
  [ -n "$wf" ] || continue
  checked=$((checked + 1))
  out="$(python3 - "$wf" <<'PY'
import re
import sys

FORBIDDEN = {"pull_request_target", "workflow_run", "issue_comment", "issues", "discussion",
             "discussion_comment"}
GRANT_RE = re.compile(r"""(^|[\s{,])["']?id-token["']?\s*:\s*["']?write(?![A-Za-z0-9_-])""", re.M)
WRITE_ALL_RE = re.compile(r"(?<![A-Za-z0-9_-])write-all(?![A-Za-z0-9_-])")

with open(sys.argv[1], encoding="utf-8") as handle:
    raw = handle.read().splitlines()
lines = [re.sub(r"\s+#.*$", "", line) for line in raw if not re.match(r"^\s*#", line)]
code = "\n".join(lines)
grant = bool(GRANT_RE.search(code) or WRITE_ALL_RE.search(code))

triggers = set()
for index, line in enumerate(lines):
    match = re.match(r"""^(?:on|"on"|'on')\s*:(.*)$""", line)
    if not match:
        continue
    rest = match.group(1).strip()
    if rest:
        triggers.update(re.findall(r"[A-Za-z_]+", rest))
        continue
    child = None
    for item in lines[index + 1:]:
        if not item.strip():
            continue
        indent = len(item) - len(item.lstrip(" "))
        text = item.strip()
        if indent == 0 and not text.startswith("- "):
            break
        if child is None:
            child = indent
        if indent != child:
            continue
        if text.startswith("- "):
            text = text[2:].strip()
        if text[:1] in "{[":
            triggers.update(re.findall(r"[A-Za-z_]+", text))
            continue
        name = re.match(r"""["']?([A-Za-z_]+)["']?""", text)
        if name:
            triggers.add(name.group(1))

print("grant=" + ("yes" if grant else "no"))
for name in sorted(triggers & FORBIDDEN):
    print("trigger " + name)
PY
)" || { echo "check-oidc-triggers: could not parse $wf" >&2; exit 2; }
  if printf '%s\n' "$out" | grep -qx 'grant=yes'; then
    bad="$(printf '%s\n' "$out" | sed -n 's/^trigger //p' | tr '\n' ' ' | sed 's/ $//')"
    if [ -n "$bad" ]; then
      echo "::error file=$wf::$wf grants id-token: write and declares the banned trigger(s): $bad (ADR-0010)" >&2
      violations=$((violations + 1))
    fi
  fi
done < <(find "$dir" -maxdepth 1 -type f \( -name '*.yml' -o -name '*.yaml' \) | LC_ALL=C sort)

if [ "$checked" -eq 0 ]; then
  echo "check-oidc-triggers: '$dir' holds no *.yml or *.yaml workflow; zero workflows checked" >&2
  exit 2
fi
if [ "$violations" -gt 0 ]; then
  echo "check-oidc-triggers: $violations of $checked workflow(s) break the ADR-0010 trigger rule" >&2
  exit 1
fi
echo "check-oidc-triggers: $checked workflow(s) in $dir follow the ADR-0010 trigger rule"
