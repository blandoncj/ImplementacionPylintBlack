from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from database import database as connection

from routes.airplane import airplane_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')

app.include_router(airplane_router, prefix='/api/airplanes', tags=['airplanes'])