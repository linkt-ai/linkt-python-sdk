# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linkt import Linkt, AsyncLinkt
from linkt.types import (
    ScheduleResponse,
    ScheduleListResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Linkt) -> None:
        schedule = client.schedule.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Linkt) -> None:
        schedule = client.schedule.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
            description="description",
            parameters={"foo": "bar"},
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Linkt) -> None:
        response = client.schedule.with_raw_response.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Linkt) -> None:
        with client.schedule.with_streaming_response.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Linkt) -> None:
        schedule = client.schedule.retrieve(
            "5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Linkt) -> None:
        response = client.schedule.with_raw_response.retrieve(
            "5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Linkt) -> None:
        with client.schedule.with_streaming_response.retrieve(
            "5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Linkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.schedule.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Linkt) -> None:
        schedule = client.schedule.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Linkt) -> None:
        schedule = client.schedule.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
            cron_expression="cron_expression",
            description="description",
            name="x",
            parameters={"foo": "bar"},
            status="active",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Linkt) -> None:
        response = client.schedule.with_raw_response.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Linkt) -> None:
        with client.schedule.with_streaming_response.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Linkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.schedule.with_raw_response.update(
                schedule_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Linkt) -> None:
        schedule = client.schedule.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Linkt) -> None:
        schedule = client.schedule.list(
            icp_id="5eb7cf5a86d9755df3a6c593",
            order=0,
            page=1,
            page_size=1,
            sort_by="sort_by",
            status="active",
            task_id="5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Linkt) -> None:
        response = client.schedule.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Linkt) -> None:
        with client.schedule.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Linkt) -> None:
        schedule = client.schedule.delete(
            "5eb7cf5a86d9755df3a6c593",
        )
        assert schedule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Linkt) -> None:
        response = client.schedule.with_raw_response.delete(
            "5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert schedule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Linkt) -> None:
        with client.schedule.with_streaming_response.delete(
            "5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Linkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.schedule.with_raw_response.delete(
                "",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
            description="description",
            parameters={"foo": "bar"},
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLinkt) -> None:
        response = await async_client.schedule.with_raw_response.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLinkt) -> None:
        async with async_client.schedule.with_streaming_response.create(
            cron_expression="cron_expression",
            icp_id="5eb7cf5a86d9755df3a6c593",
            name="x",
            task_id="5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.retrieve(
            "5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinkt) -> None:
        response = await async_client.schedule.with_raw_response.retrieve(
            "5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinkt) -> None:
        async with async_client.schedule.with_streaming_response.retrieve(
            "5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.schedule.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
            cron_expression="cron_expression",
            description="description",
            name="x",
            parameters={"foo": "bar"},
            status="active",
        )
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinkt) -> None:
        response = await async_client.schedule.with_raw_response.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinkt) -> None:
        async with async_client.schedule.with_streaming_response.update(
            schedule_id="5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.schedule.with_raw_response.update(
                schedule_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.list(
            icp_id="5eb7cf5a86d9755df3a6c593",
            order=0,
            page=1,
            page_size=1,
            sort_by="sort_by",
            status="active",
            task_id="5eb7cf5a86d9755df3a6c593",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinkt) -> None:
        response = await async_client.schedule.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinkt) -> None:
        async with async_client.schedule.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLinkt) -> None:
        schedule = await async_client.schedule.delete(
            "5eb7cf5a86d9755df3a6c593",
        )
        assert schedule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLinkt) -> None:
        response = await async_client.schedule.with_raw_response.delete(
            "5eb7cf5a86d9755df3a6c593",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert schedule is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLinkt) -> None:
        async with async_client.schedule.with_streaming_response.delete(
            "5eb7cf5a86d9755df3a6c593",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLinkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.schedule.with_raw_response.delete(
                "",
            )
