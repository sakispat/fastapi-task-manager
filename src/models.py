from typing import List, Optional


class Task:
    def __init__(self, id: int, title: str, description: Optional[str] = None):
        self.id = id
        self.title = title
        self.description = description


tasks_db: List[Task] = []
