from fastapi import FastAPI

from .api import router


app = FastAPI(
    title='Workshop',
    description='Приложение учета доходов и расходов',
    version='1.0.0'
)
app.include_router(router)
