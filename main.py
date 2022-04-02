import os
import random
import uvicorn

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn.main import logger

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")


@app.post("/", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def render_voter(request: Request):
    vote = None
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    form = await request.form()
    vote = form.get("vote")
    logger.info(f"{voter_id} -> {vote}")
    response = templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "hostname": request.client.host,
            "option_a": option_a,
            "option_b": option_b,
            "vote": vote
        }
    )
    response.set_cookie('voter_id', voter_id)

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

