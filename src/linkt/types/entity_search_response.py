# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .entity_response import EntityResponse

__all__ = ["EntitySearchResponse"]


class EntitySearchResponse(BaseModel):
    """Search response with pagination.

    All entities include enrichment fields for UI annotations.
    """

    entities: List[EntityResponse]

    page: int
    """Current page (1-based)"""

    page_size: int
    """Items per page"""

    query: str
    """Original search query"""

    total: int
    """Total matching entities"""
