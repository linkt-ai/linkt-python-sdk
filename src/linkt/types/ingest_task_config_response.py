# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IngestTaskConfigResponse"]


class IngestTaskConfigResponse(BaseModel):
    """Ingest task configuration in API responses.

    Response model for CSV enrichment task configs that excludes backend-managed
    fields from the API surface.

    Attributes:
        type: Config type discriminator (always "ingest").
        file_id: ID of the CSV file.
        primary_column: Column containing entity names.
        csv_entity_type: Entity type in CSV.
        webhook_url: Webhook URL for completion notification.
    """

    csv_entity_type: str
    """Entity type in CSV"""

    file_id: str
    """ID of the CSV file"""

    primary_column: str
    """Column containing entity names"""

    type: Optional[Literal["ingest"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
