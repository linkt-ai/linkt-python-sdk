# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .signal_csv_config_param import SignalCsvConfigParam
from .ingest_task_config_param import IngestTaskConfigParam
from .search_task_config_param import SearchTaskConfigParam
from .signal_sheet_config_param import SignalSheetConfigParam
from .signal_topic_config_param import SignalTopicConfigParam
from .profile_prompt_config_param import ProfilePromptConfigParam

__all__ = ["TaskCreateParams", "TaskConfig", "TaskConfigOnDemandIngestTaskConfigRequest"]


class TaskCreateParams(TypedDict, total=False):
    deployment_name: Required[str]
    """The Prefect deployment name for this flow"""

    description: Required[str]
    """Detailed description of what this task accomplishes"""

    flow_name: Required[str]
    """The Prefect flow name (e.g., 'search', 'ingest', 'signal')"""

    name: Required[str]
    """Human-readable name for the task"""

    icp_id: Optional[str]
    """Optional ICP ID for signal monitoring tasks"""

    prompt: Optional[str]
    """Template prompt for the task. Can include placeholders for runtime parameters."""

    task_config: Optional[TaskConfig]
    """Flow-specific task configuration with type discriminator"""


class TaskConfigOnDemandIngestTaskConfigRequest(TypedDict, total=False):
    """On-demand ingest task configuration for adding entities to existing ICPs.

    Creates a task that ingests additional entities from a CSV file into an
    existing ICP. Supports declaring which existing sheet fields can be nullable
    for the new entities and adding new enrichment fields to the sheet schema.

    Attributes:
        type: Config type discriminator (always "ingest-ondemand").
        file_id: ID of the uploaded CSV file to process.
        primary_column: Column containing entity names for matching.
        csv_entity_type: Entity type in the CSV (e.g., 'person', 'company').
        ignored_fields: Existing sheet fields allowed to be nullable for new entities.
        new_custom_fields: New enrichment fields to add to the sheet schema.
        webhook_url: Optional webhook URL for completion notification.
    """

    csv_entity_type: Required[str]
    """Entity type in the CSV (e.g., 'person', 'company')"""

    file_id: Required[str]
    """ID of the uploaded CSV file to process"""

    primary_column: Required[str]
    """Column containing entity names for matching"""

    ignored_fields: SequenceNotStr[str]
    """Existing sheet fields allowed to be nullable for new entities"""

    new_custom_fields: Iterable[Dict[str, str]]
    """New enrichment fields to add to sheet schema ({name, description})"""

    type: Literal["ingest-ondemand"]
    """Config type discriminator"""

    webhook_url: Optional[str]
    """Optional webhook URL to notify when workflow completes"""


TaskConfig: TypeAlias = Union[
    SearchTaskConfigParam,
    IngestTaskConfigParam,
    TaskConfigOnDemandIngestTaskConfigRequest,
    ProfilePromptConfigParam,
    SignalTopicConfigParam,
    SignalCsvConfigParam,
    SignalSheetConfigParam,
]
