from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import items
from .utils import ROOT

app = FastAPI()

app.include_router(items.router)
app.mount("/static", StaticFiles(directory=f"{ROOT}/static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}
