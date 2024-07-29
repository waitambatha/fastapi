
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import httpx, json

from typing import List

app = FastAPI()

# Load JSON data

response = httpx.get(url="https://api.fda.gov/food/enforcement.json?limit=10")
data = json.loads(response.content).get('results')
# Load data into memory


# Configure Jinja2 template directory
template_env = Environment(loader=FileSystemLoader('templates'))

@app.get("/", response_class=HTMLResponse)
async def get_table(request: Request):
    template = template_env.get_template('table.html')
    return template.render(data=data)

# Serve static files if needed
#app.mount("/static", StaticFiles(directory="static"), name="static")
