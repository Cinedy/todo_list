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

    # Update task name if provided
    if task_name:
        todo_list.cursor.execute("UPDATE tasks SET name = ? WHERE id = ?", (task_name, id))

    # Update task status if provided
    if status is not None:
        todo_list.cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (1 if status else 0, id))

    todo_list.conn.commit()

    return f"Task {id} updated!"

@router.delete("/delete")
def delete_task(id: int) -> str:
    todo_list = ToDoSqlService()
    todo_list.delete_task(id)
    return "Task deleted!"

