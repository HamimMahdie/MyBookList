
# MyBookList


# Dockerized Flask API for Library Management

This is a Dockerized Flask API for managing a library of books. It includes endpoints for adding, updating, retrieving, and deleting books, as well as Swagger documentation for easy API exploration.

## Requirements

- Docker

## Installation

## Clone the repository:
   git clone https://github.com/HamimMahdie/flaskApp-RESTful.git
   
## Build the Docker image:

### docker build -t my-flask-app .

## Run the Docker container:

### docker run -d -p 5000:5000 my-flask-app

## Access the API documentation:

Open a web browser and navigate to http://localhost:5000/swagger to access the Swagger UI for API documentation.


### API Endpoints
GET "/books": Get a list of all books.

POST "/books": Add a new book to the library.

GET "/books/<index>": Get details of a specific book.

PUT "/books/<index>": Update details of a specific book.

DELETE "/books/<index>": Delete a specific book.
