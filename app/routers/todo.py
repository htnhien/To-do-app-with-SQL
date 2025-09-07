from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import todo as crud
from app.schemas import todo as schemas
from app.utils.dependencies import get_db

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.post("/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db, db_todo, todo)

@router.delete("/{todo_id}", response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.delete_todo(db, db_todo)
