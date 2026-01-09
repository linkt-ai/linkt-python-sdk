# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .entity_type import EntityType
from .signal_type_config_param import SignalTypeConfigParam

__all__ = [
    "TaskUpdateParams",
    "TaskConfig",
    "TaskConfigSearchTaskConfigRequest",
    "TaskConfigIngestTaskConfigRequest",
    "TaskConfigProfilePromptConfigRequest",
    "TaskConfigSignalTopicConfigRequest",
    "TaskConfigSignalCsvConfigRequest",
    "TaskConfigSignalSheetConfigRequest",
]


class TaskUpdateParams(TypedDict, total=False):
    deployment_name: Optional[str]
    """Updated deployment name"""

    description: Optional[str]
    """Updated task description"""

    icp_id: Optional[str]
    """Updated ICP Connection"""

    name: Optional[str]
    """Updated task name"""

    prompt: Optional[str]
    """Updated task prompt template"""

    task_config: Optional[TaskConfig]
    """Updated flow-specific task configuration with type discriminator"""


class TaskConfigSearchTaskConfigRequest(TypedDict, total=False):
    """Search task configuration for finding companies and contacts.

    Creates a v3.0 search workflow that uses AI agents to discover
    entities matching your ICP criteria.

    Attributes:
        type: Config type discriminator (always "search").
        desired_contact_count: Number of contacts to find per company (minimum: 1).
        user_feedback: Optional feedback to refine search behavior.
        webhook_url: Optional webhook URL for completion notification.

    Example:
        >>> config = SearchTaskConfigRequest(desired_contact_count=5)
        >>> mongo_config = config.to_mongo_config()
        >>> mongo_config.version
        'v3.0'
    """

    desired_contact_count: int
    """Number of contacts to find per company (minimum: 1)"""

    type: Literal["search"]
    """Config type discriminator"""

    user_feedback: str
    """Optional feedback to refine search behavior"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


class TaskConfigIngestTaskConfigRequest(TypedDict, total=False):
    """CSV enrichment task configuration.

    Enriches entities from an uploaded CSV file with additional
    data discovered by AI agents.

    Attributes:
        type: Config type discriminator (always "ingest").
        file_id: ID of the uploaded CSV file to process.
        primary_column: Column containing entity names for matching.
        csv_entity_type: Entity type in the CSV (e.g., 'person', 'company').
        webhook_url: Optional webhook URL for completion notification.

    Example:
        >>> config = IngestTaskConfigRequest(file_id="abc123", primary_column="company_name", csv_entity_type="company")
    """

    csv_entity_type: Required[str]
    """Entity type in the CSV (e.g., 'person', 'company')"""

    file_id: Required[str]
    """ID of the uploaded CSV file to process"""

    primary_column: Required[str]
    """Column containing entity names for matching"""

    type: Literal["ingest"]
    """Config type discriminator"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


class TaskConfigProfilePromptConfigRequest(TypedDict, total=False):
    """Profile prompt task configuration.

    Configures a profile workflow with a custom prompt template.

    Attributes:
        type: Config type discriminator (always "profile").
        prompt: Jinja2 template for task instructions.
        webhook_url: Optional webhook URL for completion notification.

    Example:
        >>> config = ProfilePromptConfigRequest(prompt="Analyze {{ company_name }} and extract key metrics.")
    """

    prompt: Required[str]
    """Jinja2 template for task instructions"""

    type: Literal["profile"]
    """Config type discriminator"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


class TaskConfigSignalTopicConfigRequest(TypedDict, total=False):
    """Topic-based signal monitoring configuration.

    Monitors for signals based on topic criteria without requiring
    pre-existing entities.

    Attributes:
        type: Config type discriminator (always "signal-topic").
        topic_criteria: Natural language description of what to monitor.
        signal_types: Types of signals to monitor.
        entity_type: Type of entity being monitored (default: company).
        monitoring_frequency: How often to check (daily/weekly/monthly).
        geographic_filters: Optional geographic regions to focus on.
        industry_filters: Optional industries to focus on.
        company_size_filters: Optional company size criteria.
        webhook_url: Optional webhook URL for completion notification.

    Example:
        >>> config = SignalTopicConfigRequest(
        ...     topic_criteria="AI startups raising Series A",
        ...     signal_types=[SignalTypeConfig(type="funding", ...)]
        ... )
    """

    signal_types: Required[Iterable[SignalTypeConfigParam]]
    """Types of signals to monitor"""

    topic_criteria: Required[str]
    """Natural language description of what to monitor"""

    company_size_filters: Optional[SequenceNotStr[str]]
    """Company size criteria"""

    entity_type: EntityType
    """Type of entity being monitored"""

    geographic_filters: Optional[SequenceNotStr[str]]
    """Geographic regions to focus on"""

    industry_filters: Optional[SequenceNotStr[str]]
    """Industries to focus on"""

    monitoring_frequency: Literal["daily", "weekly", "monthly"]
    """How often to check for new signals"""

    type: Literal["signal-topic"]
    """Config type discriminator"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


class TaskConfigSignalCsvConfigRequest(TypedDict, total=False):
    """CSV-based signal monitoring configuration.

    Monitors signals for entities uploaded via CSV file.

    Attributes:
        type: Config type discriminator (always "signal-csv").
        file_id: ID of the uploaded CSV file.
        signal_types: Types of signals to monitor.
        entity_type: Type of entity being monitored (default: company).
        primary_column: Column containing entity names (default: "name").
        monitoring_frequency: How often to check (daily/weekly/monthly).
        webhook_url: Optional webhook URL for completion notification.

    Example:
        >>> config = SignalCSVConfigRequest(
        ...     file_id="abc123",
        ...     signal_types=[SignalTypeConfig(type="hiring_surge", ...)]
        ... )
    """

    file_id: Required[str]
    """ID of the uploaded CSV file"""

    signal_types: Required[Iterable[SignalTypeConfigParam]]
    """Types of signals to monitor"""

    entity_type: EntityType
    """Type of entity being monitored"""

    monitoring_frequency: Literal["daily", "weekly", "monthly"]
    """How often to check for new signals"""

    primary_column: str
    """Column containing entity names"""

    type: Literal["signal-csv"]
    """Config type discriminator"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


class TaskConfigSignalSheetConfigRequest(TypedDict, total=False):
    """Sheet-based signal monitoring configuration.

    Monitors signals for entities from an existing discovery ICP's sheet.

    Attributes:
        type: Config type discriminator (always "signal-sheet").
        source_icp_id: ID of the discovery ICP containing entities to monitor.
        signal_types: Types of signals to monitor.
        entity_type: Type of entity being monitored (default: company).
        entity_filters: Optional MongoDB query to filter entities.
        monitoring_frequency: How often to check (daily/weekly/monthly).
        webhook_url: Optional webhook URL for completion notification.

    Example:
        >>> config = SignalSheetConfigRequest(
        ...     source_icp_id="icp123",
        ...     signal_types=[SignalTypeConfig(type="leadership_change", ...)]
        ... )
    """

    signal_types: Required[Iterable[SignalTypeConfigParam]]
    """Types of signals to monitor"""

    source_icp_id: Required[str]
    """ID of the discovery ICP containing entities to monitor"""

    entity_filters: Optional[Dict[str, object]]
    """Optional MongoDB query to filter entities"""

    entity_type: EntityType
    """Type of entity being monitored"""

    monitoring_frequency: Literal["daily", "weekly", "monthly"]
    """How often to check for new signals"""

    type: Literal["signal-sheet"]
    """Config type discriminator"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


TaskConfig: TypeAlias = Union[
    TaskConfigSearchTaskConfigRequest,
    TaskConfigIngestTaskConfigRequest,
    TaskConfigProfilePromptConfigRequest,
    TaskConfigSignalTopicConfigRequest,
    TaskConfigSignalCsvConfigRequest,
    TaskConfigSignalSheetConfigRequest,
]
