# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from linkt import Linkt, AsyncLinkt
from linkt.types import (
    EntityResponse,
    EntityListResponse,
    EntitySearchResponse,
    EntityGetCountsResponse,
    EntityBulkUpdateStatusResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Linkt) -> None:
        entity = client.entity.retrieve(
            "entity_id",
        )
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.retrieve(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.retrieve(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Linkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entity.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Linkt) -> None:
        entity = client.entity.update(
            entity_id="entity_id",
        )
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Linkt) -> None:
        entity = client.entity.update(
            entity_id="entity_id",
            comments="comments",
            propagate_to_duplicates=True,
            propagate_to_family=True,
            status="new",
        )
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.update(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.update(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Linkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entity.with_raw_response.update(
                entity_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Linkt) -> None:
        entity = client.entity.list()
        assert_matches_type(EntityListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Linkt) -> None:
        entity = client.entity.list(
            entity_type="company",
            hide_duplicates=True,
            icp_id="icp_id",
            page=1,
            page_size=1,
            sheet_id="sheet_id",
            status=["string"],
        )
        assert_matches_type(EntityListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityListResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Linkt) -> None:
        entity = client.entity.delete(
            "entity_id",
        )
        assert entity is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.delete(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert entity is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.delete(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Linkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entity.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_update_status(self, client: Linkt) -> None:
        entity = client.entity.bulk_update_status(
            entity_ids=["string"],
            status="status",
        )
        assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_update_status_with_all_params(self, client: Linkt) -> None:
        entity = client.entity.bulk_update_status(
            entity_ids=["string"],
            status="status",
            propagate_to_duplicates=True,
            propagate_to_family=True,
        )
        assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_update_status(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.bulk_update_status(
            entity_ids=["string"],
            status="status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_update_status(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.bulk_update_status(
            entity_ids=["string"],
            status="status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export(self, client: Linkt) -> None:
        entity = client.entity.export()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_export_with_all_params(self, client: Linkt) -> None:
        entity = client.entity.export(
            entity_ids=["string"],
            entity_type="company",
            format="separate",
            icp_id="icp_id",
            sheet_id="sheet_id",
            status=["string"],
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_export(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_export(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_counts(self, client: Linkt) -> None:
        entity = client.entity.get_counts()
        assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_counts_with_all_params(self, client: Linkt) -> None:
        entity = client.entity.get_counts(
            icp_id="icp_id",
            status=["string"],
        )
        assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_counts(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.get_counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_counts(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.get_counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Linkt) -> None:
        entity = client.entity.search(
            q="x",
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Linkt) -> None:
        entity = client.entity.search(
            q="x",
            entity_type="company",
            hide_duplicates=True,
            icp_id="icp_id",
            page=1,
            page_size=1,
            sheet_id="sheet_id",
            status=["string"],
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Linkt) -> None:
        response = client.entity.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Linkt) -> None:
        with client.entity.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntitySearchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.retrieve(
            "entity_id",
        )
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.retrieve(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.retrieve(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLinkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entity.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.update(
            entity_id="entity_id",
        )
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.update(
            entity_id="entity_id",
            comments="comments",
            propagate_to_duplicates=True,
            propagate_to_family=True,
            status="new",
        )
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.update(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.update(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLinkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entity.with_raw_response.update(
                entity_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.list()
        assert_matches_type(EntityListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.list(
            entity_type="company",
            hide_duplicates=True,
            icp_id="icp_id",
            page=1,
            page_size=1,
            sheet_id="sheet_id",
            status=["string"],
        )
        assert_matches_type(EntityListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityListResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityListResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.delete(
            "entity_id",
        )
        assert entity is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.delete(
            "entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert entity is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.delete(
            "entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert entity is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLinkt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entity.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_update_status(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.bulk_update_status(
            entity_ids=["string"],
            status="status",
        )
        assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_update_status_with_all_params(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.bulk_update_status(
            entity_ids=["string"],
            status="status",
            propagate_to_duplicates=True,
            propagate_to_family=True,
        )
        assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_update_status(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.bulk_update_status(
            entity_ids=["string"],
            status="status",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_update_status(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.bulk_update_status(
            entity_ids=["string"],
            status="status",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityBulkUpdateStatusResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.export()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.export(
            entity_ids=["string"],
            entity_type="company",
            format="separate",
            icp_id="icp_id",
            sheet_id="sheet_id",
            status=["string"],
        )
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(object, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(object, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_counts(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.get_counts()
        assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_counts_with_all_params(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.get_counts(
            icp_id="icp_id",
            status=["string"],
        )
        assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_counts(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.get_counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_counts(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.get_counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetCountsResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.search(
            q="x",
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLinkt) -> None:
        entity = await async_client.entity.search(
            q="x",
            entity_type="company",
            hide_duplicates=True,
            icp_id="icp_id",
            page=1,
            page_size=1,
            sheet_id="sheet_id",
            status=["string"],
        )
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLinkt) -> None:
        response = await async_client.entity.with_raw_response.search(
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntitySearchResponse, entity, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLinkt) -> None:
        async with async_client.entity.with_streaming_response.search(
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntitySearchResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
