from fastapi import FastAPI
from utils import get_logger
from api.handler import router as api_router

logger = get_logger(__name__)

app = FastAPI(title="Virtusize ", swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(api_router)
