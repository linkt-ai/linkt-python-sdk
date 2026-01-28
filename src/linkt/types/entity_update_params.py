# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EntityUpdateParams"]


class EntityUpdateParams(TypedDict, total=False):
    comments: Optional[str]
    """Update comments (null to clear)"""

    propagate_to_duplicates: bool
    """Reflect updates to duplicate entities across ICPs (default: True)"""

    propagate_to_family: bool
    """Reflect updates to parent/child entities (default: True)"""

    status: Optional[Literal["new", "reviewed", "passed", "contacted"]]
    """Status values for entity workflow tracking.

    Transitions are user-driven (not automatic state machine):

    - new: Default for all newly created entities
    - reviewed: User has examined the entity
    - passed: Entity has been approved/qualified
    - contacted: Outreach has been initiated
    """
