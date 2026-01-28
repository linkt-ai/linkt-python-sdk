# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EntityBulkUpdateStatusParams"]


class EntityBulkUpdateStatusParams(TypedDict, total=False):
    entity_ids: Required[SequenceNotStr[str]]
    """List of entity IDs to update (1-1000 IDs)"""

    status: Required[Optional[str]]
    """New status value: new, reviewed, passed, contacted, or null to clear"""

    propagate_to_duplicates: bool
    """Reflect status to duplicate entities across ICPs (default: True)"""

    propagate_to_family: bool
    """Reflect status to parent/child of each entity (default: True)"""
