# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProfilePromptConfigResponse"]


class ProfilePromptConfigResponse(BaseModel):
    """Profile prompt configuration in API responses.

    Response model for profile prompt task configs that excludes backend-managed
    fields from the API surface.

    Attributes:
        type: Config type discriminator (always "profile").
        prompt: Task prompt template.
        webhook_url: Webhook URL for completion notification.
    """

    prompt: str
    """Task prompt template"""

    type: Optional[Literal["profile"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
