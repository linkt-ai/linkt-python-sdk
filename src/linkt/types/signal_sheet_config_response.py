# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .entity_type import EntityType
from .signal_type_config import SignalTypeConfig

__all__ = ["SignalSheetConfigResponse"]


class SignalSheetConfigResponse(BaseModel):
    """Signal sheet configuration in API responses.

    Response model for sheet-based signal monitoring configs.

    Attributes:
        type: Config type discriminator (always "signal-sheet").
        source_icp_id: Source ICP ID containing entities to monitor.
        signal_types: Types of signals to monitor.
        entity_type: Type of entity being monitored.
        entity_filters: Optional MongoDB query to filter entities.
        monitoring_frequency: How often to check for signals.
        webhook_url: Webhook URL for completion notification.
    """

    entity_type: EntityType
    """Entity type"""

    monitoring_frequency: Literal["daily", "weekly", "monthly"]
    """Monitoring frequency"""

    signal_types: List[SignalTypeConfig]
    """Signal types"""

    source_icp_id: str
    """Source ICP ID"""

    entity_filters: Optional[Dict[str, object]] = None
    """Entity filters"""

    type: Optional[Literal["signal-sheet"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
