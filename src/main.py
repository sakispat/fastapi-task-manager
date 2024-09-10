from fastapi import FastAPI, HTTPException
from typing import List
from .schemas import TaskCreate, TaskResponse
from .api import create_task, get_tasks, get_task, update_task, delete_task


app = FastAPI()


@app.post("/tasks/", response_model=TaskResponse)
def add_task(task: TaskCreate):
    return create_task(task)


@app.get("/tasks/", response_model=List[TaskResponse])
def list_tasks():
    return get_tasks()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    task = get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def modify_task(task_id: int, task: TaskCreate):
    updated_task = update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/tasks/{task_id}", response_model=dict)
def remove_task(task_id: int):
    if not delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
