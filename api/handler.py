import re
import requests

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import status
from utils import get_logger

router = APIRouter()

logger = get_logger(__name__)


class WordCountPayload(BaseModel):
    word: str
    url: str


class WordCountResponse(BaseModel):
    status: str
    count: int


@router.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"Hello": "World"}


def search_keyword(keyword, content) -> list[str]:
    results = re.findall(rf"\b{keyword}\b", content, flags=re.IGNORECASE)
    return results


@router.post("/wordcount", status_code=status.HTTP_200_OK, response_model=WordCountResponse)
async def wordcount(payload: WordCountPayload):
    logger.info(f"PAYLOAD: {payload}")

    response = requests.get(payload.url.strip())
    content = response.content.decode("utf-8")

    results = search_keyword(payload.word, content)
    logger.info(f"results: {results}")

    return WordCountResponse(
        status="ok",
        count=len(results)
    )
