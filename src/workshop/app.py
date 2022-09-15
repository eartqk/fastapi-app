from fastapi import FastAPI

from .api import router


app = FastAPI(
    title='Workshop',
    description='Applications for accounting of income and outcome',
    version='1.0.0',
)
app.include_router(router)
