# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ScheduleCreateParams"]


class ScheduleCreateParams(TypedDict, total=False):
    cron_expression: Required[str]
    """Cron expression (5 parts: minute hour day month day_of_week).

    Must be daily, weekly, or monthly.
    """

    icp_id: Required[str]
    """ICP context for execution"""

    name: Required[str]
    """Schedule name"""

    task_id: Required[str]
    """Task to execute"""

    description: Optional[str]
    """Schedule description"""

    parameters: Dict[str, object]
    """Execution parameters"""
