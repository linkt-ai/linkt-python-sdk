# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityResponse"]


class EntityResponse(BaseModel):
    """Response model for single entity.

    IMPORTANT: Enrichment fields (sheet_name, entity_type, icp_id) are
    ALWAYS populated to support UI annotations. Excludes embedding data
    for HTTP efficiency.
    """

    id: str
    """Entity ID"""

    created_at: datetime
    """Creation timestamp"""

    data: Dict[str, object]
    """Entity attribute data"""

    entity_type: str
    """Entity type (company, person, etc.)"""

    icp_id: str
    """ICP ID (via sheet)"""

    sheet_id: str
    """Sheet this entity belongs to"""

    sheet_name: str
    """Name of parent sheet"""

    updated_at: datetime
    """Last update timestamp"""

    comments: Optional[str] = None
    """User comments"""

    parent_id: Optional[str] = None
    """Parent entity ID (for hierarchical entities)"""

    status: Optional[str] = None
    """Entity workflow status: new, reviewed, passed, contacted, or null"""
