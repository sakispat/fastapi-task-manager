from typing import List, Optional
from .models import Task, tasks_db
from .schemas import TaskCreate


def create_task(task: TaskCreate) -> Task:
    task_id = len(tasks_db) + 1
    new_task = Task(id=task_id, **task.dict())
    tasks_db.append(new_task)
    return new_task


def get_tasks() -> List[Task]:
    return tasks_db


def get_task(task_id: int) -> Optional[Task]:
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None


def update_task(task_id: int, task_update: TaskCreate) -> Optional[Task]:
    for task in tasks_db:
        if task.id == task_id:
            task.title = task_update.title
            task.description = task_update.description
            return task
    return None


def delete_task(task_id: int) -> bool:
    global tasks_db
    tasks_db = [task for task in tasks_db if task.id != task_id]
    return len(tasks_db) < len(tasks_db)
