from fastapi import FastAPI

from controllers.search import router

app = FastAPI()

app.include_router(router, prefix="/search")
