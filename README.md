# FDA Food Enforcement Search

This project is a FastAPI-based web application that allows users to search FDA food enforcement reports. Users can search for reports based on various fields and view the results in a table format.

## Features

- Displays the latest FDA food enforcement reports.
- Allows users to search for reports by specific fields and terms.
- Displays search results in a table format.
- Uses an FDA API key for accessing the data.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/fda-food-enforcement-search.git
    cd fda-food-enforcement-search
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    uvicorn main:app --reload
    ```

5. **Access the application:**

    Open your browser and navigate to `http://localhost:8000`.

## Usage

### Home Page

- The home page displays the latest FDA food enforcement reports.
- A search form is available at the top of the page.

### Search

- Users can search for reports by selecting a field and entering a search term.
- The search results will be displayed in a table format.

### Search URL

- Users can also perform searches directly from the URL.
- Example: `http://localhost:8000/search?field=report_date&term=2020`

## Project Structure

- `main.py`: Main FastAPI application file.
- `templates/`: Directory containing HTML templates.
  - `table.html`: Template for the home page.
  - `search_results.html`: Template for displaying search results.
- `requirements.txt`: List of required Python packages.

## API Key

- The application uses an FDA API key for accessing the data.
- The API key is included in the requests to the FDA API.

## Dependencies

- `fastapi`: FastAPI framework.
- `httpx`: HTTP client for making requests.
- `jinja2`: Templating engine.
- `uvicorn`: ASGI server for running the application.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [FDA API](https://open.fda.gov/) for providing the data.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [Jinja2](https://jinja.palletsprojects.com/) for the templating engine.

## Contributing

If you have any suggestions or improvements, feel free to open an issue or create a pull request.

