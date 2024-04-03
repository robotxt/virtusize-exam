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

    assert response.status_code == status_code


def test_search_keyword():
    content = "<html><body><p>fit<p><br /><p>fitting</p><span>fitting</span></body></html>"
    result = search_keyword("fit", content)
    assert 1 == len(result)
