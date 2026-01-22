# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SearchTaskConfigResponse"]


class SearchTaskConfigResponse(BaseModel):
    """Search task configuration in API responses.

    Response model for search task configs that excludes backend-managed fields
    (version, config_type) from the API surface.

    Attributes:
        type: Config type discriminator (always "search").
        desired_contact_count: Number of contacts to find per company.
        user_feedback: Feedback to refine search behavior.
        webhook_url: Webhook URL for completion notification.
    """

    desired_contact_count: int
    """Number of contacts to find per company"""

    user_feedback: str
    """Feedback to refine search behavior"""

    type: Optional[Literal["search"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
