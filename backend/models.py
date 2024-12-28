import sqlite3
from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = Field(None)
    name: str = Field(...)
    status: bool = Field(False)
    
class ToDoSqlService:
    def __init__(self, db_name="todo.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()

    def add_task(self, task_name):
        self.cursor.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (task_name, 0))
        self.conn.commit()
        print(f"Task added: {task_name}")

    def view_tasks(self) -> list[Task]:
        self.cursor.execute("SELECT id, name, done FROM tasks")
        tasks = self.cursor.fetchall()
        print(tasks)
        return [Task(id=task["id"], name=task["name"], done=task["done"] == 1) for task in tasks]
        
    def mark_done(self, task_id):
        try:
            self.cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
            if self.cursor.rowcount == 0:
                print(f"No task found with ID: {task_id}")
            else:
                print(f"Task {task_id} marked as done.")
        except sqlite3.Error as e:
            print(f"Error updating task: {e}")
        
    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        print(f"Deleted task with ID: {task_id}")
    
    def close_connection(self):
        self.conn.close()