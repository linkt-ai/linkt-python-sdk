# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    icp_id: Optional[str]
    """Filter by ICP"""

    order: Optional[int]
    """Sort order: -1 descending, 1 ascending"""

    page: int
    """Page number (1-based)"""

    page_size: int
    """Items per page (max 100)"""

    sort_by: Optional[str]
    """Field to sort by (e.g., 'created_at')"""

    status: Optional[Literal["active", "paused", "disabled"]]
    """Schedule status values.

    ACTIVE: Schedule is eligible for execution PAUSED: Temporarily suspended but can
    be resumed DISABLED: Permanently disabled (requires manual intervention)
    """

    task_id: Optional[str]
    """Filter by task"""
