# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .signal_csv_config_response import SignalCsvConfigResponse
from .ingest_task_config_response import IngestTaskConfigResponse
from .search_task_config_response import SearchTaskConfigResponse
from .signal_sheet_config_response import SignalSheetConfigResponse
from .signal_topic_config_response import SignalTopicConfigResponse
from .ingest_prompt_config_response import IngestPromptConfigResponse
from .profile_prompt_config_response import ProfilePromptConfigResponse

__all__ = ["TaskListResponse", "Task", "TaskTaskConfig", "TaskTaskConfigOnDemandIngestTaskConfigResponse"]


class TaskTaskConfigOnDemandIngestTaskConfigResponse(BaseModel):
    """On-demand ingest task configuration in API responses.

    Response model for on-demand ingest task configs that excludes backend-managed
    fields from the API surface.

    Attributes:
        type: Config type discriminator (always "ingest-ondemand").
        file_id: ID of the CSV file.
        primary_column: Column containing entity names.
        csv_entity_type: Entity type in CSV.
        ignored_fields: Existing sheet fields allowed to be nullable.
        new_custom_fields: New enrichment fields added to sheet schema.
        webhook_url: Webhook URL for completion notification.
    """

    csv_entity_type: str
    """Entity type in CSV"""

    file_id: str
    """ID of the CSV file"""

    primary_column: str
    """Column containing entity names"""

    ignored_fields: Optional[List[str]] = None
    """Existing sheet fields allowed to be nullable"""

    new_custom_fields: Optional[List[Dict[str, str]]] = None
    """New enrichment fields added to sheet schema"""

    type: Optional[Literal["ingest-ondemand"]] = None

    webhook_url: Optional[str] = None
    """Webhook URL for completion notification"""


TaskTaskConfig: TypeAlias = Annotated[
    Union[
        SearchTaskConfigResponse,
        IngestTaskConfigResponse,
        TaskTaskConfigOnDemandIngestTaskConfigResponse,
        IngestPromptConfigResponse,
        ProfilePromptConfigResponse,
        SignalTopicConfigResponse,
        SignalCsvConfigResponse,
        SignalSheetConfigResponse,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class Task(BaseModel):
    """Response model for task data.

    Uses TaskConfigResponse discriminated union for proper OpenAPI schema
    generation with type-based discrimination.

    Attributes:
        id: Task ID.
        name: Task name.
        description: Task description.
        icp_id: Task ICP ID.
        flow_name: Prefect flow name.
        deployment_name: Prefect deployment name.
        prompt: Template prompt for the task.
        task_config: Flow-specific task configuration.
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
    """

    id: str
    """Task ID"""

    created_at: datetime
    """Creation timestamp"""

    deployment_name: str
    """Prefect deployment name"""

    description: str
    """Task description"""

    flow_name: str
    """Prefect flow name"""

    name: str
    """Task name"""

    updated_at: datetime
    """Last update timestamp"""

    icp_id: Optional[str] = None
    """Task ICP ID"""

    prompt: Optional[str] = None
    """Template prompt for the task. Can include placeholders for runtime parameters."""

    task_config: Optional[TaskTaskConfig] = None
    """Flow-specific task configuration"""


class TaskListResponse(BaseModel):
    """Response model for paginated task list.

    Attributes:
        tasks: List of tasks.
        total: Total number of tasks matching filters.
        page: Current page number (1-based).
        page_size: Number of items per page.
    """

    page: int
    """Current page number (1-based)"""

    page_size: int
    """Number of items per page"""

    tasks: List[Task]
    """List of tasks"""

    total: int
    """Total number of tasks matching filters"""
