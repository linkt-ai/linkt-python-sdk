# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EntityResponse", "DuplicateInfo", "DuplicateInfoDuplicateIcp"]


class DuplicateInfoDuplicateIcp(BaseModel):
    """Info about an ICP containing a duplicate entity.

    Used in DuplicateInfo to show which ICPs contain duplicate instances
    of the same entity.
    """

    icp_id: str
    """ICP ID"""

    icp_name: str
    """ICP name"""


class DuplicateInfo(BaseModel):
    """Duplicate status information for an entity.

    Indicates whether an entity is part of a duplicate group and its role:
    - Primary entities: is_primary=True, has duplicate_entity_ids and duplicate_icps
    - Duplicate entities: is_duplicate=True, has primary_entity_id and primary_icp_name

    For entities that have no duplicates, this field will be None/null in the
    EntityResponse.
    """

    is_duplicate: bool
    """Whether this entity is a duplicate (not the primary)"""

    is_primary: bool
    """Whether this entity is the primary in a duplicate group"""

    duplicate_count: Optional[int] = None
    """Number of duplicate entities (primary only)"""

    duplicate_entity_ids: Optional[List[str]] = None
    """IDs of duplicate entities (primary only)"""

    duplicate_icps: Optional[List[DuplicateInfoDuplicateIcp]] = None
    """ICPs containing duplicates (primary only)"""

    primary_entity_id: Optional[str] = None
    """ID of the primary entity (duplicate only)"""

    primary_icp_name: Optional[str] = None
    """ICP name of the primary entity (duplicate only)"""


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

    duplicate_info: Optional[DuplicateInfo] = None
    """Duplicate status information for an entity.

    Indicates whether an entity is part of a duplicate group and its role:

    - Primary entities: is_primary=True, has duplicate_entity_ids and duplicate_icps
    - Duplicate entities: is_duplicate=True, has primary_entity_id and
      primary_icp_name

    For entities that have no duplicates, this field will be None/null in the
    EntityResponse.
    """

    parent_id: Optional[str] = None
    """Parent entity ID (for hierarchical entities)"""

    status: Optional[Literal["new", "reviewed", "passed", "contacted"]] = None
    """Workflow status (new, reviewed, passed, contacted)"""
