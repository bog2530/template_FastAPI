from contextlib import asynccontextmanager

import aiohttp
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import Settings, settings
from api import list_of_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    aiohttp_session = aiohttp.ClientSession()
    app.aiohttp_session = aiohttp_session
    yield
    await aiohttp_session.close()


def get_app() -> FastAPI:
    def bind_routes(application: FastAPI, setting: Settings) -> None:
        for route in list_of_routes:
            application.include_router(route, prefix="/api")

    application = FastAPI(
        title="RAG",
        docs_url="/",
        openapi_url="/openapi",
        version="1.0.0",
        lifespan=lifespan,
    )
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
