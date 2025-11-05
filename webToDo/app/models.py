import logging
from typing import List


class Task:
    # Клас представляє одну задачу
    def __init__(self, title: str, description: str, status: str = "заплановано"):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self) -> dict:
        # метод перетворює об’єкт Task в словник
        return {"title": self.title, "description": self.description, "status": self.status}

    @classmethod
    def from_dict(cls, data: dict):
        # метод відновлює об’єкт Task із словника
        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            status=data.get("status", "заплановано")
        )


class TaskManager:
    # Клас для керуваняя списком задач
    def __init__(self):
        # Ініціалізація списку задач
        self.tasks: List[Task] = []
        logging.info("Було створено менеджер задач")

    def add_task(self, title: str, description: str, status: str = "заплановано"):
        # Метод додає нову задачу до списку
        self.tasks.append(Task(title, description, status))
        logging.info(f"Було додано задачу: {title}")

    def edit_task(self, index: int, title: str = None, description: str = None, status: str = None):
        # Метод дозволяє редагувати задачу по індексу задачі
        try:
            task = self.tasks[index]
            # для логування зберігаємо попередні значення
            previous_title = task.title
            previous_description = task.description
            previous_status = task.status

            # зміна назви/опису/статусу при введенні
            if title:
                task.title = title
                logging.info(f"Було змінено назву задачі {previous_title} на {task.title}")
            if description:
                task.description = description
                logging.info(
                    f"Було змінено опис задачі {previous_title} з {previous_description} на {task.description}")
            if status:
                task.status = status
                logging.info(f"Було змінено статус задачі {previous_title} з {previous_status} на {task.description}")
        except IndexError:
            print("Задачі не існує")
            logging.warning("Було здійснено спробу редагувати неіснуючу задачу")

    def delete_task(self, index: int):
        # Метод дозволяє видалити задачу по індексу задачі
        try:
            deleted_task = self.tasks[index]
            del self.tasks[index]
            logging.info(f"Було видалено задачу: {deleted_task.title}")
        except IndexError:
            print("Невірний номер")
            logging.warning("Було здійснено спробу видалити задачу з неіснуючим індексом")

    def move_task(self, old_index: int, new_index: int):
        # Метод дозволяє змінити порядок задач
        try:
            # вирізаємо задачу з одного місця
            task = self.tasks.pop(old_index)
            # розміщуємо задачу на нове місце
            self.tasks.insert(new_index, task)
            logging.info(f"Було переміщено задачу {task.title} з позиції {old_index} на позицію {new_index}")
        except IndexError:
            print("Неможливо змінити порядок")
            logging.warning("Було здійснено спробу перемістити неіснуючу задачу")

    def show_tasks(self):
        # Метод для виведення всього списку задач
        if not self.tasks:
            print("Задачі відсутні")
            logging.info("Було отримано запит на виведення списку задач. Список задач порожній")
            return
        logging.info(f"Успішно виведено повний список задач")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def to_dict_list(self) -> List[dict]:
        # Метод перетворює всі задачі в список словників для збереження у файл
        return [t.to_dict() for t in self.tasks]

    def from_dict_list(self, data: List[dict]):
        # Метод відновлює задачі зі списку словників після завантаження з файлу
        self.tasks = [Task.from_dict(item) for item in data]

    def get_task(self, index: int):
        # Метод для отримання задачі по індексу
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def clear(self):
        # метод для очищення списку задач
        self.tasks = []
