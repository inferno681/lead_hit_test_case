import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import router
from app.db import mongo
from app.service import FormService
from config import config

log = logging.getLogger('uvicorn')


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Запуск и остановка сервиса."""
    form_service = FormService(mongo)
    app.state.form_service = form_service
    log.info('Service started')

    yield

    mongo.close()

    log.info('Connections closed')


tags_metadata = [
    config.service.tags_metadata,
]

app = FastAPI(
    title=config.service.title,
    description=config.service.description,
    openapi_tags=tags_metadata,
    lifespan=lifespan,
    debug=config.service.debug,
)

app.include_router(router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=config.service.host,
        port=config.service.port,
    )  # noqa:WPS432
