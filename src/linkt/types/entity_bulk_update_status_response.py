# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EntityBulkUpdateStatusResponse"]


class EntityBulkUpdateStatusResponse(BaseModel):
    """Response for bulk status update operation.

    WHY: Reports both success count and specific failures so the client
    knows exactly which entities were updated and which failed.
    """

    updated_count: int
    """Number of entities successfully updated"""

    failed_ids: Optional[List[str]] = None
    """Entity IDs that failed to update (invalid format or not found)"""
