from fastapi import APIRouter
from models import ToDoSqlService, Task
from typing import Optional

router = APIRouter(prefix="/tasks")

@router.get("/all")
def get_tasks() -> list[Task]:
    todo_list = ToDoSqlService()
    tasks = todo_list.view_tasks()
    return tasks

@router.post("/create")
def create_task(task_name: str) -> str:
    todo_list = ToDoSqlService()
    todo_list.add_task(task_name=task_name)
    return "Task added."

@router.patch("/update")
def update_task(id: int, task_name: Optional[str] = None, status: Optional[bool] = None) -> str:
    todo_list = ToDoSqlService()
    todo_list.mark_done(id)
    #Todo: fix this function later
    return "Task updated!"

@router.delete("/delete")
def delete_task(id: int) -> str:
    todo_list = ToDoSqlService()
    todo_list.delete_task(id)
    return "Task deleted!"

