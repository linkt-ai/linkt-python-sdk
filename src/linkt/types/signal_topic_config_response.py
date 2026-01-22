# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .entity_type import EntityType
from .signal_type_config import SignalTypeConfig

__all__ = ["SignalTopicConfigResponse"]


class SignalTopicConfigResponse(BaseModel):
    """Signal topic configuration in API responses.

    Response model for topic-based signal monitoring configs.

    Attributes:
        type: Config type discriminator (always "signal-topic").
        topic_criteria: Topic criteria for monitoring.
        signal_types: Types of signals to monitor.
        entity_type: Type of entity being monitored.
        monitoring_frequency: How often to check for signals.
        geographic_filters: Geographic regions to focus on.
        industry_filters: Industries to focus on.
        company_size_filters: Company size criteria.
        webhook_url: Webhook URL for completion notification.
    """

    entity_type: EntityType
    """Entity type"""

    monitoring_frequency: Literal["daily", "weekly", "monthly"]
    """Monitoring frequency"""

    signal_types: List[SignalTypeConfig]
    """Signal types"""

    topic_criteria: str
    """Topic criteria"""

    company_size_filters: Optional[List[str]] = None
    """Size filters"""

    geographic_filters: Optional[List[str]] = None
    """Geographic filters"""

    industry_filters: Optional[List[str]] = None
    """Industry filters"""

    type: Optional[Literal["signal-topic"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""
