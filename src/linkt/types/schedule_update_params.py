# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    cron_expression: Optional[str]
    """Updated cron expression"""

    description: Optional[str]
    """Updated description"""

    name: Optional[str]
    """Updated schedule name"""

    parameters: Optional[Dict[str, object]]
    """Updated execution parameters"""

    status: Optional[Literal["active", "paused", "disabled"]]
    """Schedule status values.

    ACTIVE: Schedule is eligible for execution PAUSED: Temporarily suspended but can
    be resumed DISABLED: Permanently disabled (requires manual intervention)
    """
