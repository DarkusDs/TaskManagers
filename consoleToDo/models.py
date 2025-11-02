from typing import List


class Task:
    def __init__(self, title: str, description: str, status: str = "заплановано"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.status}\n {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, status: str = "заплановано"):
        self.tasks.append(Task(title, description, status))

    def edit_task(self, index: int, title: str = None, description: str = None, status: str = None):
        try:
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if status:
                task.status = status
        except IndexError:
            print("Задачі не існує")

    def delete_task(self, index: int):
        try:
            del self.tasks[index]
        except IndexError:
            print("Невірний номер")

    def move_task(self, old_index: int, new_index: int):
        try:
            task = self.tasks.pop(old_index)
            self.tasks.insert(new_index, task)
        except IndexError:
            print("Неможливо змінити порядок")

    def show_tasks(self):
        if not self.tasks:
            print("Задачі відсутні")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def to_dict_list(self):
        result = []
        for i in self.tasks:
            item = {
                "title": i.title,
                "description": i.description,
                "status": i.status
            }
            result.append(item)
        return result

    def from_dict_list(self, data):
        tasks = []
        for item in data:
            task = Task(
                title=item["title"],
                description=item["description"],
                status=item["status"]
            )
            tasks.append(task)
        self.tasks = tasks
