# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .signal_csv_config_response import SignalCsvConfigResponse
from .ingest_task_config_response import IngestTaskConfigResponse
from .search_task_config_response import SearchTaskConfigResponse
from .signal_sheet_config_response import SignalSheetConfigResponse
from .signal_topic_config_response import SignalTopicConfigResponse
from .ingest_prompt_config_response import IngestPromptConfigResponse
from .profile_prompt_config_response import ProfilePromptConfigResponse

__all__ = ["TaskCreateResponse", "TaskConfig"]

TaskConfig: TypeAlias = Annotated[
    Union[
        SearchTaskConfigResponse,
        IngestTaskConfigResponse,
        IngestPromptConfigResponse,
        ProfilePromptConfigResponse,
        SignalTopicConfigResponse,
        SignalCsvConfigResponse,
        SignalSheetConfigResponse,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class TaskCreateResponse(BaseModel):
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

    task_config: Optional[TaskConfig] = None
    """Flow-specific task configuration"""
