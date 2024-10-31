from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.controllers import link_controller


app = FastAPI()

app.include_router(link_controller.router)

@app.get("/")
def main(req: Request):
    return "Go to /docs for Swagger UI"

