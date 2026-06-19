# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .entity_type import EntityType

__all__ = ["EntityListParams"]


class EntityListParams(TypedDict, total=False):
    entity_type: Optional[EntityType]
    """Filter by entity type"""

    external_id: Optional[str]
    """Filter by an external record identifier (e.g.

    a Salesforce Account Id). Resolves to the org's entities carrying this
    external_id across all ICPs.
    """

    external_source: str
    """External system that owns external_id (default: 'salesforce')."""

    fields: Optional[str]
    """Comma-separated list of data fields to include (e.g., 'name,company,title').

    Returns all fields if omitted.
    """

    hide_duplicates: bool
    """Hide duplicate entities (show only primaries)"""

    icp_id: Optional[SequenceNotStr[str]]
    """Filter by ICP ID(s) - supports multiple"""

    page: int
    """Page number (1-based)"""

    page_size: int
    """Items per page"""

    sheet_id: Optional[str]
    """Filter by sheet ID"""

    status: Optional[SequenceNotStr[str]]
    """Filter by status values (supports multiple: ?status=new&status=reviewed)"""
