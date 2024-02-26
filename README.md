
# MyBookList

## Dockerized Flask API for Library Management

This is a Dockerized Flask API for managing a library of books. It includes endpoints for adding, updating, retrieving, and deleting books, as well as Swagger documentation for easy API exploration.

## Journey

Throughout my journey, I initially delved into Spring Boot with Maven, following along with tutorials from Amigoscode on YouTube. However, I hit a roadblock when encountering unusual errors on my device, despite extensive troubleshooting efforts. This prompted me to pivot to Python and Flask, where I found building applications to be more straightforward, especially with the help of YouTube tutorials to guide me through Flask, which was new to me. Despite the detour, I aim to revisit Spring Boot to further my learning and resolve the errors I encountered, as I believe it holds valuable knowledge and skills worth mastering.

## Requirements

- Docker
- Python
- Laptop

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/HamimMahdie/flaskApp-RESTful.git
   ```

2. Build the Docker image:

   ```
   docker build -t my-flask-app .
   ```

3. Run the Docker container:

   ```
   docker run -d -p 5000:5000 my-flask-app
   ```

4. Access the API documentation:

   Open a web browser and navigate to [http://localhost:5000/swagger](http://localhost:5000/swagger) to access the Swagger UI for API documentation.

## API Endpoints

- **GET "/books"**: Get a list of all books.
- **POST "/books"**: Add a new book to the library.
- **GET "/books/<index>"**: Get details of a specific book.
- **PUT "/books/<index>"**: Update details of a specific book.
- **DELETE "/books/<index>"**: Delete a specific book.
```
