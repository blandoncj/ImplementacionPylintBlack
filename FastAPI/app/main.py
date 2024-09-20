"""
This module defines a FastAPI application with multiple routes and an asynchronous context manager 
to manage the database connection lifespan.
"""

from contextlib import asynccontextmanager
from database import database as connection
from routes.airplane import airplane_router
from routes.cook_book import cookbook_router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Asynchronous context manager to manage the database connection lifespan for the FastAPI app.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Pauses execution for the app's lifespan, ensuring the database connection is opened
        at the start and closed at the end.

    Behavior:
        - Opens the database connection if it's closed when the app starts.
        - Ensures the database connection is closed after the app finishes running.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/", include_in_schema=False)
def root():
    """
    Redirects the root URL ("/") to the FastAPI documentation page ("/docs").

    Returns:
        RedirectResponse: A response that redirects the user to the FastAPI docs.
    """
    return RedirectResponse(url="/docs")


app.include_router(airplane_router, prefix="/api/airplanes", tags=["airplanes"])
app.include_router(cookbook_router, prefix="/api/cookbooks", tags=["cookbooks"])
