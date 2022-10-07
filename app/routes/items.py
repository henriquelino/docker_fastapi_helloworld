import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..utils import ROOT

router = APIRouter(prefix='', tags=["callback pages"])

templates = Jinja2Templates(directory=f'{ROOT}/templates')

logger = logging.getLogger(__name__)


@router.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    logger.critical("read_item funcion")
    return templates.TemplateResponse("item.html", {
        "request": request,
        "id": id
    })
