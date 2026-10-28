from dataclasses import dataclass
from enum import Enum
from uuid import UUID


class TaskStatus(Enum):
    ToDo = "To Do"
    InProgress = "In Progress"
    Done = "Done"

@dataclass
class Task:
    id: UUID
    description: str
    created_at: datetime
    schedule_for: datetime
    status: TaskStatus





