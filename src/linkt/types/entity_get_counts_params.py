# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["EntityGetCountsParams"]


class EntityGetCountsParams(TypedDict, total=False):
    hide_duplicates: bool
    """Exclude duplicate entities from counts (show only primaries)"""

    icp_id: Optional[SequenceNotStr[str]]
    """Filter by ICP ID(s) - supports multiple"""

    status: Optional[SequenceNotStr[str]]
    """Filter by status values (supports multiple: ?status=new&status=passed)"""
