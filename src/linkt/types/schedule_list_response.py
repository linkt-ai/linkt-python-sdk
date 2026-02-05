# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .schedule_response import ScheduleResponse

__all__ = ["ScheduleListResponse"]


class ScheduleListResponse(BaseModel):
    """Response model for paginated schedule list.

    Attributes:
        schedules: List of schedules.
        total: Total number of schedules matching filters.
        page: Current page number (1-based).
        page_size: Number of items per page.
    """

    page: int
    """Current page number (1-based)"""

    page_size: int
    """Number of items per page"""

    schedules: List[ScheduleResponse]
    """List of schedules"""

    total: int
    """Total number of schedules matching filters"""
