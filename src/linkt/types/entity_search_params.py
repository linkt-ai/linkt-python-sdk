# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .entity_type import EntityType

__all__ = ["EntitySearchParams"]


class EntitySearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    entity_type: Optional[EntityType]
    """Valid entity types for sheets."""

    hide_duplicates: bool
    """Hide duplicate entities (show only primaries)"""

    icp_id: Optional[SequenceNotStr[str]]
    """Filter by ICP ID(s) - supports multiple"""

    page: int
    """Page number"""

    page_size: int
    """Items per page"""

    sheet_id: Optional[str]
    """Filter by sheet ID"""

    status: Optional[SequenceNotStr[str]]
    """Filter by status values (supports multiple: ?status=new&status=reviewed)"""
