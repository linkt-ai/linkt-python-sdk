# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ScheduleResponse"]


class ScheduleResponse(BaseModel):
    """Response model for schedule data.

    Attributes:
        id: Schedule ID.
        name: Schedule name.
        task_id: Task ID.
        icp_id: ICP ID.
        cron_expression: Cron expression.
        status: Schedule status.
        description: Optional description.
        parameters: Execution parameters.
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
    """

    id: str
    """Schedule ID"""

    created_at: datetime
    """Creation timestamp"""

    cron_expression: str
    """Cron expression"""

    icp_id: str
    """ICP ID"""

    name: str
    """Schedule name"""

    status: str
    """Schedule status"""

    task_id: str
    """Task ID"""

    updated_at: datetime
    """Last update timestamp"""

    description: Optional[str] = None
    """Description"""

    parameters: Optional[Dict[str, object]] = None
    """Execution parameters"""
