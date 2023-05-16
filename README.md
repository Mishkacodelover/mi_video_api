# Mi video api

This is a README document for Mi video api, a Python-based API built using the FastAPI library. The API provides various endpoints to perform specific tasks and interact with data.

## Features

- Easy-to-use API built with FastAPI.
- Supports various HTTP methods (GET, POST, PUT, DELETE) for different operations.
- JSON-based communication format.
- Utilizes Python's asyncio for high performance and scalability.
- Supports data validation and serialization using Pydantic models.
- Includes automatic interactive API documentation with Swagger UI.
- Implements security features like API key authentication, JWT-based authentication, etc.

## Installation

To set up the API on your local machine, follow these steps:

1. Clone the repository:

```sh

git clone https://github.com/your-username/my-awesome-api.git
```

2. Navigate to the project directory:

```sh

cd mi_video_api
```

3. Create a virtual environment (optional but recommended):

```sh
python -m venv env
```

4. Activate the virtual environment:

For Windows:

```sh
venv\Scripts\activate
```

For macOS/Linux:

```sh
source env/bin/activate
```

5. Install the required dependencies:

```sh
pip install -r requirements.txt
```

6. Start the API server:

```sh
uvicorn main:app --reload
```

The API should now be running on http://localhost:8000.

### Usage

Once the API server is up and running, you can interact with the API using HTTP requests. Here are the API endpoints:

GET /movies: Retrieve a list of all movies.
GET /movies/{id}: Get details of a specific movie by ID.
GET /movies/: Get details of all movies by filtered by category.
POST /movies: Create a new movie.
PUT /movies{id}: Update an existing movie.
DELETE /movie/{id}: Delete a movie.
POST/login: obtain authorization by bearer token to log into privata routes.

For more detailed documentation and to explore the API interactively, visit the Swagger UI at http://localhost:8000/docs in your web browser.

### Configuration

The API can be configured by modifying the config.py file. This file contains various settings such as database connection details, authentication mechanisms, logging configurations, etc. Customize these settings according to your requirements.
