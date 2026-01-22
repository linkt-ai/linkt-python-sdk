# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .entity_response import EntityResponse

__all__ = ["EntityListResponse"]


class EntityListResponse(BaseModel):
    """Paginated list response for entities.

    All entities include enrichment fields (sheet_name, entity_type, icp_id)
    to support UI annotations without additional API calls.
    """

    entities: List[EntityResponse]

    page: int
    """Current page (1-based)"""

    page_size: int
    """Items per page"""

    total: int
    """Total matching entities (before pagination)"""
