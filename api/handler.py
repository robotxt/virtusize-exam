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
    word: str
    count: int


@router.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"Hello": "World"}


@router.post("/wordcount", status_code=WordCountResponse)
async def wordcount(payload: WordCountPayload):
    logger.info("PAYLOAD: %s", payload)
    return WordCountResponse(
        word="hello",
        count=5
    )
