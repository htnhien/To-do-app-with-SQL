from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import todo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do App", version="1.0.0")

app.include_router(todo.router)