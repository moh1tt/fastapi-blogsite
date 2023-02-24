from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="Blogs/templates/")
router = APIRouter(tags=['Porfolio'])


@router.get('/')
def homepage(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})



