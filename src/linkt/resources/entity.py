# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    EntityType,
    entity_list_params,
    entity_export_params,
    entity_search_params,
    entity_update_params,
    entity_get_counts_params,
    entity_bulk_update_status_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.entity_type import EntityType
from ..types.entity_response import EntityResponse
from ..types.entity_list_response import EntityListResponse
from ..types.entity_search_response import EntitySearchResponse
from ..types.entity_get_counts_response import EntityGetCountsResponse
from ..types.entity_bulk_update_status_response import EntityBulkUpdateStatusResponse

__all__ = ["EntityResource", "AsyncEntityResource"]


class EntityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EntityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#with_streaming_response
        """
        return EntityResourceWithStreamingResponse(self)

    def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityResponse:
        """
        Get a single entity by ID with enrichment.

        Returns the entity with sheet_name, entity_type, icp_id, and duplicate_info
        populated. duplicate_info is null if the entity has no duplicates across ICPs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/v1/entity/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityResponse,
        )

    def update(
        self,
        entity_id: str,
        *,
        comments: Optional[str] | Omit = omit,
        status: Optional[Literal["new", "reviewed", "passed", "contacted"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityResponse:
        """
        Update entity status or comments.

        Only status and comments can be updated via this endpoint. Use status=null to
        clear status, comments=null to clear comments.

        Status must be one of: new, reviewed, passed, contacted, or null.

        Args:
          comments: Update comments (null to clear)

          status: Update workflow status (new, reviewed, passed, contacted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._put(
            f"/v1/entity/{entity_id}",
            body=maybe_transform(
                {
                    "comments": comments,
                    "status": status,
                },
                entity_update_params.EntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityResponse,
        )

    def list(
        self,
        *,
        entity_type: Optional[EntityType] | Omit = omit,
        hide_duplicates: bool | Omit = omit,
        icp_id: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sheet_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityListResponse:
        """
        Get paginated list of entities with filtering.

        Supports filtering by:

        - icp_id: Entities in sheets belonging to an ICP
        - sheet_id: Entities in a specific sheet
        - entity_type: Entities of a specific type (company, person, etc.)
        - status: Filter by workflow status (supports multiple:
          ?status=new&status=reviewed) Valid values: new, reviewed, passed, contacted,
          null
        - hide_duplicates: When true, only show primary entities (filter out duplicates)

        All results include enrichment fields for UI annotations.

        Args:
          entity_type: Valid entity types for sheets.

          hide_duplicates: Hide duplicate entities (show only primaries)

          icp_id: Filter by ICP ID

          page: Page number (1-based)

          page_size: Items per page

          sheet_id: Filter by sheet ID

          status: Filter by status values (supports multiple: ?status=new&status=reviewed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/entity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_type": entity_type,
                        "hide_duplicates": hide_duplicates,
                        "icp_id": icp_id,
                        "page": page,
                        "page_size": page_size,
                        "sheet_id": sheet_id,
                        "status": status,
                    },
                    entity_list_params.EntityListParams,
                ),
            ),
            cast_to=EntityListResponse,
        )

    def delete(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an entity by ID.

        This is a hard delete - the entity will be permanently removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/entity/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk_update_status(
        self,
        *,
        entity_ids: SequenceNotStr[str],
        status: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBulkUpdateStatusResponse:
        """
        Update status for multiple entities at once.

        Accepts a list of entity IDs and a status value. The status can be:

        - "new", "reviewed", "passed", "contacted" (valid workflow statuses)
        - null (to clear the status)

        Returns the count of successfully updated entities and any failed IDs. Entities
        may fail to update if they have an invalid ID format or don't exist.

        WHY: Bulk operations enable users to update status for many entities at once
        (e.g., mark all search results as "reviewed"), improving workflow efficiency
        versus N individual PUT calls. Uses batch_update_by_filter for single database
        roundtrip efficiency.

        Args:
          entity_ids: List of entity IDs to update (1-1000 IDs)

          status: New status value: new, reviewed, passed, contacted, or null to clear

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/entity/status/bulk",
            body=maybe_transform(
                {
                    "entity_ids": entity_ids,
                    "status": status,
                },
                entity_bulk_update_status_params.EntityBulkUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBulkUpdateStatusResponse,
        )

    def export(
        self,
        *,
        entity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        entity_type: Optional[EntityType] | Omit = omit,
        format: Literal["separate", "combined"] | Omit = omit,
        icp_id: Optional[str] | Omit = omit,
        sheet_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export entities as CSV.

        Supports two formats:

        **separate** (default):

        - One row per entity
        - Standard flat export
        - All entity types exported independently

        **combined**:

        - Pre-joined parent-child rows
        - Requires icp_id parameter
        - Child entity columns appear first, followed by parent columns
        - Columns prefixed with entity type (e.g., "Person Name", "Company Industry")
        - Parent data repeats for each child (one row per child)
        - Orphan parents (no children) appear as rows with empty child columns

        **Excluded Fields** (both formats):

        - id, sheet_id, parent_id, icp_id, entity_type, sheet_name, comments

        **Included Fields**:

        - All data.\\** fields (the actual enrichment data)
        - status, created_at, updated_at

        **Filtering**:

        - status: Filter by workflow status (supports multiple:
          ?status=new&status=contacted) Valid values: new, reviewed, passed, contacted,
          null

        Args: icp_id: Filter by ICP ID (REQUIRED for format=combined) sheet_id: Filter
        by sheet ID entity_type: Filter by entity type (ignored for format=combined)
        entity_ids: Export specific entity IDs status: Filter by status values (multiple
        allowed) format: Export format - "separate" (default) or "combined"

        Returns: StreamingResponse with CSV content

        Raises: HTTPException 400: format=combined without icp_id, or invalid status
        value HTTPException 404: ICP, sheet, or entities not found

        Args:
          entity_ids: Specific entity IDs

          entity_type: Valid entity types for sheets.

          format: Export format: 'separate' (default) or 'combined' (joined parent-child rows)

          icp_id: Filter by ICP ID

          sheet_id: Filter by sheet ID

          status: Filter by status values (supports multiple: ?status=new&status=contacted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/entity/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "format": format,
                        "icp_id": icp_id,
                        "sheet_id": sheet_id,
                        "status": status,
                    },
                    entity_export_params.EntityExportParams,
                ),
            ),
            cast_to=object,
        )

    def get_counts(
        self,
        *,
        icp_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityGetCountsResponse:
        """
        Get entity counts grouped by entity_type.

        Returns the count of entities for each entity_type (company, person, etc.)
        across the organization. Supports optional filtering by ICP or status.

        Additional filtering:

        - status: Filter by workflow status (supports multiple:
          ?status=new&status=reviewed) Valid values: new, reviewed, passed, contacted,
          null

        Used by Entity Master List for accurate tab navigation counts.

        Args:
          icp_id: Filter by ICP ID

          status: Filter by status values (supports multiple: ?status=new&status=passed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/entity/counts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "icp_id": icp_id,
                        "status": status,
                    },
                    entity_get_counts_params.EntityGetCountsParams,
                ),
            ),
            cast_to=EntityGetCountsResponse,
        )

    def search(
        self,
        *,
        q: str,
        entity_type: Optional[EntityType] | Omit = omit,
        hide_duplicates: bool | Omit = omit,
        icp_id: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sheet_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitySearchResponse:
        """
        Search entities by text query.

        Uses MongoDB Atlas Search for fuzzy text matching on entity names and company
        fields. Results are sorted by relevance.

        Scope of search determined by filters:

        - sheet_id: Search within specific sheet
        - icp_id: Search across ICP sheets
        - No filters: Search org-wide

        Additional filtering:

        - status: Filter by workflow status (supports multiple:
          ?status=new&status=reviewed) Valid values: new, reviewed, passed, contacted,
          null
        - hide_duplicates: When true, only show primary entities

        Args:
          q: Search query

          entity_type: Valid entity types for sheets.

          hide_duplicates: Hide duplicate entities (show only primaries)

          icp_id: Filter by ICP ID

          page: Page number

          page_size: Items per page

          sheet_id: Filter by sheet ID

          status: Filter by status values (supports multiple: ?status=new&status=reviewed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/entity/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "entity_type": entity_type,
                        "hide_duplicates": hide_duplicates,
                        "icp_id": icp_id,
                        "page": page,
                        "page_size": page_size,
                        "sheet_id": sheet_id,
                        "status": status,
                    },
                    entity_search_params.EntitySearchParams,
                ),
            ),
            cast_to=EntitySearchResponse,
        )


class AsyncEntityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEntityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#with_streaming_response
        """
        return AsyncEntityResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityResponse:
        """
        Get a single entity by ID with enrichment.

        Returns the entity with sheet_name, entity_type, icp_id, and duplicate_info
        populated. duplicate_info is null if the entity has no duplicates across ICPs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/v1/entity/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityResponse,
        )

    async def update(
        self,
        entity_id: str,
        *,
        comments: Optional[str] | Omit = omit,
        status: Optional[Literal["new", "reviewed", "passed", "contacted"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityResponse:
        """
        Update entity status or comments.

        Only status and comments can be updated via this endpoint. Use status=null to
        clear status, comments=null to clear comments.

        Status must be one of: new, reviewed, passed, contacted, or null.

        Args:
          comments: Update comments (null to clear)

          status: Update workflow status (new, reviewed, passed, contacted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._put(
            f"/v1/entity/{entity_id}",
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "status": status,
                },
                entity_update_params.EntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityResponse,
        )

    async def list(
        self,
        *,
        entity_type: Optional[EntityType] | Omit = omit,
        hide_duplicates: bool | Omit = omit,
        icp_id: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sheet_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityListResponse:
        """
        Get paginated list of entities with filtering.

        Supports filtering by:

        - icp_id: Entities in sheets belonging to an ICP
        - sheet_id: Entities in a specific sheet
        - entity_type: Entities of a specific type (company, person, etc.)
        - status: Filter by workflow status (supports multiple:
          ?status=new&status=reviewed) Valid values: new, reviewed, passed, contacted,
          null
        - hide_duplicates: When true, only show primary entities (filter out duplicates)

        All results include enrichment fields for UI annotations.

        Args:
          entity_type: Valid entity types for sheets.

          hide_duplicates: Hide duplicate entities (show only primaries)

          icp_id: Filter by ICP ID

          page: Page number (1-based)

          page_size: Items per page

          sheet_id: Filter by sheet ID

          status: Filter by status values (supports multiple: ?status=new&status=reviewed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/entity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_type": entity_type,
                        "hide_duplicates": hide_duplicates,
                        "icp_id": icp_id,
                        "page": page,
                        "page_size": page_size,
                        "sheet_id": sheet_id,
                        "status": status,
                    },
                    entity_list_params.EntityListParams,
                ),
            ),
            cast_to=EntityListResponse,
        )

    async def delete(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an entity by ID.

        This is a hard delete - the entity will be permanently removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/entity/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk_update_status(
        self,
        *,
        entity_ids: SequenceNotStr[str],
        status: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBulkUpdateStatusResponse:
        """
        Update status for multiple entities at once.

        Accepts a list of entity IDs and a status value. The status can be:

        - "new", "reviewed", "passed", "contacted" (valid workflow statuses)
        - null (to clear the status)

        Returns the count of successfully updated entities and any failed IDs. Entities
        may fail to update if they have an invalid ID format or don't exist.

        WHY: Bulk operations enable users to update status for many entities at once
        (e.g., mark all search results as "reviewed"), improving workflow efficiency
        versus N individual PUT calls. Uses batch_update_by_filter for single database
        roundtrip efficiency.

        Args:
          entity_ids: List of entity IDs to update (1-1000 IDs)

          status: New status value: new, reviewed, passed, contacted, or null to clear

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/entity/status/bulk",
            body=await async_maybe_transform(
                {
                    "entity_ids": entity_ids,
                    "status": status,
                },
                entity_bulk_update_status_params.EntityBulkUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBulkUpdateStatusResponse,
        )

    async def export(
        self,
        *,
        entity_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        entity_type: Optional[EntityType] | Omit = omit,
        format: Literal["separate", "combined"] | Omit = omit,
        icp_id: Optional[str] | Omit = omit,
        sheet_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export entities as CSV.

        Supports two formats:

        **separate** (default):

        - One row per entity
        - Standard flat export
        - All entity types exported independently

        **combined**:

        - Pre-joined parent-child rows
        - Requires icp_id parameter
        - Child entity columns appear first, followed by parent columns
        - Columns prefixed with entity type (e.g., "Person Name", "Company Industry")
        - Parent data repeats for each child (one row per child)
        - Orphan parents (no children) appear as rows with empty child columns

        **Excluded Fields** (both formats):

        - id, sheet_id, parent_id, icp_id, entity_type, sheet_name, comments

        **Included Fields**:

        - All data.\\** fields (the actual enrichment data)
        - status, created_at, updated_at

        **Filtering**:

        - status: Filter by workflow status (supports multiple:
          ?status=new&status=contacted) Valid values: new, reviewed, passed, contacted,
          null

        Args: icp_id: Filter by ICP ID (REQUIRED for format=combined) sheet_id: Filter
        by sheet ID entity_type: Filter by entity type (ignored for format=combined)
        entity_ids: Export specific entity IDs status: Filter by status values (multiple
        allowed) format: Export format - "separate" (default) or "combined"

        Returns: StreamingResponse with CSV content

        Raises: HTTPException 400: format=combined without icp_id, or invalid status
        value HTTPException 404: ICP, sheet, or entities not found

        Args:
          entity_ids: Specific entity IDs

          entity_type: Valid entity types for sheets.

          format: Export format: 'separate' (default) or 'combined' (joined parent-child rows)

          icp_id: Filter by ICP ID

          sheet_id: Filter by sheet ID

          status: Filter by status values (supports multiple: ?status=new&status=contacted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/entity/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "entity_ids": entity_ids,
                        "entity_type": entity_type,
                        "format": format,
                        "icp_id": icp_id,
                        "sheet_id": sheet_id,
                        "status": status,
                    },
                    entity_export_params.EntityExportParams,
                ),
            ),
            cast_to=object,
        )

    async def get_counts(
        self,
        *,
        icp_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityGetCountsResponse:
        """
        Get entity counts grouped by entity_type.

        Returns the count of entities for each entity_type (company, person, etc.)
        across the organization. Supports optional filtering by ICP or status.

        Additional filtering:

        - status: Filter by workflow status (supports multiple:
          ?status=new&status=reviewed) Valid values: new, reviewed, passed, contacted,
          null

        Used by Entity Master List for accurate tab navigation counts.

        Args:
          icp_id: Filter by ICP ID

          status: Filter by status values (supports multiple: ?status=new&status=passed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/entity/counts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "icp_id": icp_id,
                        "status": status,
                    },
                    entity_get_counts_params.EntityGetCountsParams,
                ),
            ),
            cast_to=EntityGetCountsResponse,
        )

    async def search(
        self,
        *,
        q: str,
        entity_type: Optional[EntityType] | Omit = omit,
        hide_duplicates: bool | Omit = omit,
        icp_id: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sheet_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitySearchResponse:
        """
        Search entities by text query.

        Uses MongoDB Atlas Search for fuzzy text matching on entity names and company
        fields. Results are sorted by relevance.

        Scope of search determined by filters:

        - sheet_id: Search within specific sheet
        - icp_id: Search across ICP sheets
        - No filters: Search org-wide

        Additional filtering:

        - status: Filter by workflow status (supports multiple:
          ?status=new&status=reviewed) Valid values: new, reviewed, passed, contacted,
          null
        - hide_duplicates: When true, only show primary entities

        Args:
          q: Search query

          entity_type: Valid entity types for sheets.

          hide_duplicates: Hide duplicate entities (show only primaries)

          icp_id: Filter by ICP ID

          page: Page number

          page_size: Items per page

          sheet_id: Filter by sheet ID

          status: Filter by status values (supports multiple: ?status=new&status=reviewed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/entity/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "entity_type": entity_type,
                        "hide_duplicates": hide_duplicates,
                        "icp_id": icp_id,
                        "page": page,
                        "page_size": page_size,
                        "sheet_id": sheet_id,
                        "status": status,
                    },
                    entity_search_params.EntitySearchParams,
                ),
            ),
            cast_to=EntitySearchResponse,
        )


class EntityResourceWithRawResponse:
    def __init__(self, entity: EntityResource) -> None:
        self._entity = entity

        self.retrieve = to_raw_response_wrapper(
            entity.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entity.update,
        )
        self.list = to_raw_response_wrapper(
            entity.list,
        )
        self.delete = to_raw_response_wrapper(
            entity.delete,
        )
        self.bulk_update_status = to_raw_response_wrapper(
            entity.bulk_update_status,
        )
        self.export = to_raw_response_wrapper(
            entity.export,
        )
        self.get_counts = to_raw_response_wrapper(
            entity.get_counts,
        )
        self.search = to_raw_response_wrapper(
            entity.search,
        )


class AsyncEntityResourceWithRawResponse:
    def __init__(self, entity: AsyncEntityResource) -> None:
        self._entity = entity

        self.retrieve = async_to_raw_response_wrapper(
            entity.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entity.update,
        )
        self.list = async_to_raw_response_wrapper(
            entity.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entity.delete,
        )
        self.bulk_update_status = async_to_raw_response_wrapper(
            entity.bulk_update_status,
        )
        self.export = async_to_raw_response_wrapper(
            entity.export,
        )
        self.get_counts = async_to_raw_response_wrapper(
            entity.get_counts,
        )
        self.search = async_to_raw_response_wrapper(
            entity.search,
        )


class EntityResourceWithStreamingResponse:
    def __init__(self, entity: EntityResource) -> None:
        self._entity = entity

        self.retrieve = to_streamed_response_wrapper(
            entity.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entity.update,
        )
        self.list = to_streamed_response_wrapper(
            entity.list,
        )
        self.delete = to_streamed_response_wrapper(
            entity.delete,
        )
        self.bulk_update_status = to_streamed_response_wrapper(
            entity.bulk_update_status,
        )
        self.export = to_streamed_response_wrapper(
            entity.export,
        )
        self.get_counts = to_streamed_response_wrapper(
            entity.get_counts,
        )
        self.search = to_streamed_response_wrapper(
            entity.search,
        )


class AsyncEntityResourceWithStreamingResponse:
    def __init__(self, entity: AsyncEntityResource) -> None:
        self._entity = entity

        self.retrieve = async_to_streamed_response_wrapper(
            entity.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entity.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entity.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entity.delete,
        )
        self.bulk_update_status = async_to_streamed_response_wrapper(
            entity.bulk_update_status,
        )
        self.export = async_to_streamed_response_wrapper(
            entity.export,
        )
        self.get_counts = async_to_streamed_response_wrapper(
            entity.get_counts,
        )
        self.search = async_to_streamed_response_wrapper(
            entity.search,
        )
