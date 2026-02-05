# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import schedule_list_params, schedule_create_params, schedule_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.schedule_response import ScheduleResponse
from ..types.schedule_list_response import ScheduleListResponse

__all__ = ["ScheduleResource", "AsyncScheduleResource"]


class ScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#with_streaming_response
        """
        return ScheduleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cron_expression: str,
        icp_id: str,
        name: str,
        task_id: str,
        description: Optional[str] | Omit = omit,
        parameters: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleResponse:
        """
        Create a new schedule.

        The cron expression must be a daily, weekly, or monthly pattern. For signal
        tasks, the cron frequency must match the task's monitoring_frequency.

        Args:
          cron_expression: Cron expression (5 parts: minute hour day month day_of_week). Must be daily,
              weekly, or monthly.

          icp_id: ICP context for execution

          name: Schedule name

          task_id: Task to execute

          description: Schedule description

          parameters: Execution parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/schedule",
            body=maybe_transform(
                {
                    "cron_expression": cron_expression,
                    "icp_id": icp_id,
                    "name": name,
                    "task_id": task_id,
                    "description": description,
                    "parameters": parameters,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleResponse,
        )

    def retrieve(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleResponse:
        """
        Get a specific schedule by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._get(
            f"/v1/schedule/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleResponse,
        )

    def update(
        self,
        schedule_id: str,
        *,
        cron_expression: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        parameters: Optional[Dict[str, object]] | Omit = omit,
        status: Optional[Literal["active", "paused", "disabled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleResponse:
        """Update a schedule.

        Only provided fields will be updated.

        The cron expression is validated for
        frequency restrictions.

        Args:
          cron_expression: Updated cron expression

          description: Updated description

          name: Updated schedule name

          parameters: Updated execution parameters

          status: Schedule status values.

              ACTIVE: Schedule is eligible for execution PAUSED: Temporarily suspended but can
              be resumed DISABLED: Permanently disabled (requires manual intervention)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._patch(
            f"/v1/schedule/{schedule_id}",
            body=maybe_transform(
                {
                    "cron_expression": cron_expression,
                    "description": description,
                    "name": name,
                    "parameters": parameters,
                    "status": status,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleResponse,
        )

    def list(
        self,
        *,
        icp_id: Optional[str] | Omit = omit,
        order: Optional[int] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "paused", "disabled"]] | Omit = omit,
        task_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        List schedules with pagination and optional filters.

        Args:
          icp_id: Filter by ICP

          order: Sort order: -1 descending, 1 ascending

          page: Page number (1-based)

          page_size: Items per page (max 100)

          sort_by: Field to sort by (e.g., 'created_at')

          status: Schedule status values.

              ACTIVE: Schedule is eligible for execution PAUSED: Temporarily suspended but can
              be resumed DISABLED: Permanently disabled (requires manual intervention)

          task_id: Filter by task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/schedule",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "icp_id": icp_id,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "status": status,
                        "task_id": task_id,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    def delete(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a schedule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/schedule/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/linkt-ai/linkt-python-sdk#with_streaming_response
        """
        return AsyncScheduleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cron_expression: str,
        icp_id: str,
        name: str,
        task_id: str,
        description: Optional[str] | Omit = omit,
        parameters: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleResponse:
        """
        Create a new schedule.

        The cron expression must be a daily, weekly, or monthly pattern. For signal
        tasks, the cron frequency must match the task's monitoring_frequency.

        Args:
          cron_expression: Cron expression (5 parts: minute hour day month day_of_week). Must be daily,
              weekly, or monthly.

          icp_id: ICP context for execution

          name: Schedule name

          task_id: Task to execute

          description: Schedule description

          parameters: Execution parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/schedule",
            body=await async_maybe_transform(
                {
                    "cron_expression": cron_expression,
                    "icp_id": icp_id,
                    "name": name,
                    "task_id": task_id,
                    "description": description,
                    "parameters": parameters,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleResponse,
        )

    async def retrieve(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleResponse:
        """
        Get a specific schedule by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._get(
            f"/v1/schedule/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleResponse,
        )

    async def update(
        self,
        schedule_id: str,
        *,
        cron_expression: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        parameters: Optional[Dict[str, object]] | Omit = omit,
        status: Optional[Literal["active", "paused", "disabled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleResponse:
        """Update a schedule.

        Only provided fields will be updated.

        The cron expression is validated for
        frequency restrictions.

        Args:
          cron_expression: Updated cron expression

          description: Updated description

          name: Updated schedule name

          parameters: Updated execution parameters

          status: Schedule status values.

              ACTIVE: Schedule is eligible for execution PAUSED: Temporarily suspended but can
              be resumed DISABLED: Permanently disabled (requires manual intervention)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._patch(
            f"/v1/schedule/{schedule_id}",
            body=await async_maybe_transform(
                {
                    "cron_expression": cron_expression,
                    "description": description,
                    "name": name,
                    "parameters": parameters,
                    "status": status,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleResponse,
        )

    async def list(
        self,
        *,
        icp_id: Optional[str] | Omit = omit,
        order: Optional[int] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "paused", "disabled"]] | Omit = omit,
        task_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        List schedules with pagination and optional filters.

        Args:
          icp_id: Filter by ICP

          order: Sort order: -1 descending, 1 ascending

          page: Page number (1-based)

          page_size: Items per page (max 100)

          sort_by: Field to sort by (e.g., 'created_at')

          status: Schedule status values.

              ACTIVE: Schedule is eligible for execution PAUSED: Temporarily suspended but can
              be resumed DISABLED: Permanently disabled (requires manual intervention)

          task_id: Filter by task

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/schedule",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "icp_id": icp_id,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "status": status,
                        "task_id": task_id,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    async def delete(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a schedule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/schedule/{schedule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ScheduleResourceWithRawResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_raw_response_wrapper(
            schedule.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schedule.retrieve,
        )
        self.update = to_raw_response_wrapper(
            schedule.update,
        )
        self.list = to_raw_response_wrapper(
            schedule.list,
        )
        self.delete = to_raw_response_wrapper(
            schedule.delete,
        )


class AsyncScheduleResourceWithRawResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_raw_response_wrapper(
            schedule.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schedule.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            schedule.update,
        )
        self.list = async_to_raw_response_wrapper(
            schedule.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schedule.delete,
        )


class ScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_streamed_response_wrapper(
            schedule.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schedule.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            schedule.update,
        )
        self.list = to_streamed_response_wrapper(
            schedule.list,
        )
        self.delete = to_streamed_response_wrapper(
            schedule.delete,
        )


class AsyncScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_streamed_response_wrapper(
            schedule.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schedule.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            schedule.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schedule.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedule.delete,
        )
