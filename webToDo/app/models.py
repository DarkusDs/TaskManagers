from typing import List


class Task:
    def __init__(self, title: str, description: str, status: str = "заплановано"):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self) -> dict:
        return {"title": self.title, "description": self.description, "status": self.status}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            status=data.get("status", "заплановано")
        )


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, status: str = "заплановано"):
        self.tasks.append(Task(title, description, status))

    def edit_task(self, index: int, title: str = None, description: str = None, status: str = None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if status is not None:
                task.status = status
            return True
        return False

    def delete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return True
        return False

    def move_task(self, old_index: int, new_index: int) -> bool:
        if 0 <= old_index < len(self.tasks) and 0 <= new_index <= len(self.tasks):
            task = self.tasks.pop(old_index)
            self.tasks.insert(new_index, task)
            return True
        return False

    def to_dict_list(self) -> List[dict]:
        return [t.to_dict() for t in self.tasks]

    def from_dict_list(self, data: List[dict]):
        self.tasks = [Task.from_dict(item) for item in data]

    def get_task(self, index: int):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def clear(self):
        self.tasks = []
