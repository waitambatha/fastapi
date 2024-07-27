Install Required Packages: Ensure you have FastAPI, Uvicorn, and Jinja2 installed. Jinja2 is a templating engine for Python.

bash
Copy code
pip install fastapi uvicorn jinja2
Prepare Your JSON Data: For simplicity, place your JSON data in a file called data.json.

Set Up FastAPI with Jinja2 Templates:

Set Up FastAPI with Jinja2 Templates:

Here’s how you can set up your FastAPI application to serve an HTML page with the data in a table.

python
Copy code
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import json
from typing import List

app = FastAPI()

# Load JSON data
def load_data(file_path: str) -> List[dict]:
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data.get("results", [])

# Load data into memory
data = load_data('data.json')

# Configure Jinja2 template directory
template_env = Environment(loader=FileSystemLoader('templates'))

@app.get("/", response_class=HTMLResponse)
async def get_table(request: Request):
    template = template_env.get_template('table.html')
    return template.render(data=data)

# Serve static files if needed
app.mount("/static", StaticFiles(directory="static"), name="static")
Create the Jinja2 Template:

Create a folder named templates in your project directory, and inside it, create a file named table.html. This file will contain the HTML structure to display your table.

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recall Data Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Recall Data Table</h1>
    <table>
        <thead>
            <tr>
                <th>Country</th>
                <th>City</th>
                <th>Address 1</th>
                <th>Address 2</th>
                <th>Product Description</th>
                <th>Product Quantity</th>
                <th>Reason for Recall</th>
                <th>Recall Number</th>
                <th>Report Date</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for item in data %}
            <tr>
                <td>{{ item.country }}</td>
                <td>{{ item.city }}</td>
                <td>{{ item.address_1 }}</td>
                <td>{{ item.address_2 }}</td>
                <td>{{ item.product_description }}</td>
                <td>{{ item.product_quantity }}</td>
                <td>{{ item.reason_for_recall }}</td>
                <td>{{ item.recall_number }}</td>
                <td>{{ item.report_date }}</td>
                <td>{{ item.status }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
Run Your FastAPI Application:

Use Uvicorn to run your FastAPI app.

bash
Copy code
uvicorn your_script_name:app --reload
Replace your_script_name with the name of your Python file (excluding the .py extension).

View the Table:

Open your browser and navigate to http://127.0.0.1:8000/. You should see a table rendered with the data from your JSON file.

Summary
Load the JSON data from a file.
Set up FastAPI with a route to serve the HTML page.
Create a Jinja2 template to render the table.
Run the FastAPI server and view the results in your browser.
This setup will dynamically load and display the recall data in a tabular format on a web page served by FastAPI.
