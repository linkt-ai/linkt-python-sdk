# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["EntityGetCountsResponse"]


class EntityGetCountsResponse(BaseModel):
    """Response model for entity counts by type.

    Returns counts grouped by entity_type with an aggregate total.
    Used by Entity Master List for tab navigation counts.
    """

    total: int
    """Sum of all entity counts"""

    counts: Optional[Dict[str, int]] = None
    """Entity counts keyed by entity_type (company, person, etc.)"""
