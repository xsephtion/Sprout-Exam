# SAIL Technical Exam

## Introduction

Backend: Python + FastAPI
Frontend: Javascript & VueJS

Objective: Create a simple CRUD Application using VueJS and FastAPI

## Getting Started

## Docker

### Building the Docker Image

To run the application within a Docker container, you need to build a Docker image first. Use the following command to build the image:

```bash
docker-compose up -d  --build
```

### Starting the Docker Container
Once you have built the Docker image, you can start a Docker container with the following command:

```bash
docker-compose up
```


To run the backend application locally without docker, follow these steps:

1. Change directory to backend folder

2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application using `uvicorn`:

   ```bash
   uvicorn main:app --reload --port 5000
   ```

   This will start the application on port 5000 with automatic reloading enabled.


To run the frontend application locally without docker, follow these steps:

1. Change directory to frontend folder

2. Install the required dependencies using `npm`:

   ```bash
   npm instsall
   ```

3. Run the application using `npm serve dev`:

   ```bash
   npm serve dev
   ```

   This will start the application on port 8080 with automatic reloading enabled.


<!-- ## Running Tests

To run the tests for the application, you can use `pytest`. First, ensure that `pytest` is installed in your virtual environment:

```bash
pip install pytest
```

Then, execute the tests by running:

```bash
pytest tests/test_main.py
``` -->





## Usage

After starting the application or the Docker container, you can access the backend by navigating to http://localhost:5000 and http://localhost:8080/ for front-end/vuejs

To check the API documentation navigate to http://localhost:5000/docs

