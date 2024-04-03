import pytest
import httpx
from httpx import AsyncClient
from fastapi import status
from main import app
from api.handler import search_keyword


@pytest.mark.parametrize(
    "payload, status_code",
    (
        (
            {"word": "fit", "url": "https://www.virtusize.jp/"},
            status.HTTP_200_OK,
        ),
    ),
)
@pytest.mark.asyncio
async def test_wordcount(payload: dict, status_code: int):
    async with AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test",
        headers={"Content-Type": "application/json"}
    ) as ac:
        response = await ac.post("/wordcount", json=payload)

    json_response = response.json()

    assert response.status_code == status_code
    assert json_response["status"] == "ok"
    assert json_response["count"] != 0


def test_search_keyword_one_result():
    content = "<html><body><p>fit<p><br /><p>fitting</p><span>fitting</span></body></html>"
    result = search_keyword("fit", content)
    assert 1 == len(result)


def test_search_keyword_two_result():
    content = "<html><body><p>fitting</p><p>fit<p><br /><p>fit</p><span>fits</span></body></html>"
    result = search_keyword("fit", content)
    assert 2 == len(result)
