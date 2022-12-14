from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import items, index
from .utils import BASE_DIR

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


app.include_router(items.router)
app.include_router(index.router)
