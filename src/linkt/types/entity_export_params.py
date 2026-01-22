# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .entity_type import EntityType

__all__ = ["EntityExportParams"]


class EntityExportParams(TypedDict, total=False):
    entity_ids: Optional[SequenceNotStr[str]]
    """Specific entity IDs"""

    entity_type: Optional[EntityType]
    """Valid entity types for sheets."""

    format: Literal["separate", "combined"]
    """Export format: 'separate' (default) or 'combined' (joined parent-child rows)"""

    icp_id: Optional[str]
    """Filter by ICP ID"""

    sheet_id: Optional[str]
    """Filter by sheet ID"""

    status: Optional[SequenceNotStr[str]]
    """Filter by status values (supports multiple: ?status=new&status=contacted)"""
