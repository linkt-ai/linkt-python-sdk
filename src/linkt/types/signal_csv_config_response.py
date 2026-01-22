# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .entity_type import EntityType
from .signal_type_config import SignalTypeConfig

__all__ = ["SignalCsvConfigResponse"]


class SignalCsvConfigResponse(BaseModel):
    """Signal CSV configuration in API responses.

    Response model for CSV-based signal monitoring configs.

    Attributes:
        type: Config type discriminator (always "signal-csv").
        file_id: CSV file ID.
        signal_types: Types of signals to monitor.
        entity_type: Type of entity being monitored.
        primary_column: Primary column for entity names.
        monitoring_frequency: How often to check for signals.
        webhook_url: Webhook URL for completion notification.
    """

    entity_type: EntityType
    """Entity type"""

    file_id: str
    """CSV file ID"""

    monitoring_frequency: Literal["daily", "weekly", "monthly"]
    """Monitoring frequency"""

    primary_column: str
    """Primary column"""

    signal_types: List[SignalTypeConfig]
    """Signal types"""

    type: Optional[Literal["signal-csv"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
