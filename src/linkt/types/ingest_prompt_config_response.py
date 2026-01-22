# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IngestPromptConfigResponse"]


class IngestPromptConfigResponse(BaseModel):
    """Ingest prompt configuration in API responses.

    Response model for prompt-based ingest task configs that excludes backend-managed
    fields from the API surface. This is for simple prompt-based ingest workflows,
    distinct from IngestTaskConfigResponse which is for CSV enrichment tasks.

    Attributes:
        type: Config type discriminator (always "ingest-prompt").
        prompt: Task prompt template.
        webhook_url: Webhook URL for completion notification.
    """

    prompt: str
    """Task prompt template"""

    type: Optional[Literal["ingest-prompt"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
