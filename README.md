# To-Do App

A simple FastAPI-based To-Do List API.

## Features

- Create, read, update, and delete to-do items
- Uses SQLAlchemy and SQLite by default
- Docker support

## Project Structure

```
app/
  main.py
  core/
    config.py
  crud/
    todo.py
  db/
    database.py
    models.py
  routers/
    todo.py
  schemas/
    todo.py
  utils/
    dependencies.py
Dockerfile
requirements.txt
```

## Getting Started

### Local Development

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the app:**
    ```sh
    uvicorn app.main:app --reload
    ```

3. **Access the API docs:**
    - Open [http://localhost:8000/docs](http://localhost:8000/docs)

### Using Docker

1. **Build the image:**
    ```sh
    docker build -t todo-app .
    ```

2. **Run the container:**
    ```sh
    docker run -p 8000:8000 todo-app
    ```

## API Endpoints

- `GET /todos/` - List all todos
- `GET /todos/{todo_id}` - Get a todo by ID
- `POST /todos/` - Create a new todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

## Configuration

- Database URL can be set via the `DATABASE_URL` environment variable (see `app/core/config.py`).

---

Made with FastAPI & SQLAlchemy.