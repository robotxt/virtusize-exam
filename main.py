from fastapi import FastAPI
from utils import get_logger
from api.handler import router as api_router

logger = get_logger(__name__)

app = FastAPI(title="Stuff And Nonsense API", version="0.4")

app.include_router(api_router)
