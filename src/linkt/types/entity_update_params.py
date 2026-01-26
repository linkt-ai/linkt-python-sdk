# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EntityUpdateParams"]


class EntityUpdateParams(TypedDict, total=False):
    comments: Optional[str]
    """Update comments (null to clear)"""

    status: Optional[Literal["new", "reviewed", "passed", "contacted"]]
    """Update workflow status (new, reviewed, passed, contacted)"""
