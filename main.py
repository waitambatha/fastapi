from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import httpx, json

app = FastAPI()

# Define the API key
API_KEY = "67bRQBaxKC64IcD37Srl2H0IDWbU1OX6ocFDvC1N"

# Load JSON data
response = httpx.get(url=f"https://api.fda.gov/food/enforcement.json?api_key={API_KEY}&limit=10")
data = json.loads(response.content).get('results')

# Configure Jinja2 template directory
template_env = Environment(loader=FileSystemLoader('templates'))


@app.get("/", response_class=HTMLResponse)
async def get_table(request: Request):
    template = template_env.get_template('table.html')
    return template.render(data=data)


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, field: str = Query(...), term: str = Query(...)):
    base_url = "https://api.fda.gov/food/enforcement.json"
    query = f"{base_url}?api_key={API_KEY}&search={field}:{term}&limit=100"
    response = httpx.get(url=query)
    search_data = json.loads(response.content).get('results', [])

    template = template_env.get_template('search_results.html')
    return template.render(data=search_data)

# Serve static files if needed
# app.mount("/static", StaticFiles(directory="static"), name="static")
