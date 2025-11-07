import logging
from models import TaskManager
from storage import save_to_file, load_from_file, delete_file

# Налаштування системи логування
logger = logging.getLogger() # головний логер
logger.setLevel(logging.INFO) # рівень логування
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s") # формат повідомлень в лог файлі
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8") # логування у файл
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) # підключення до логера

# ініціалізація менеджера задач
manager = TaskManager()


def show_menu():
    # метод для виведення головного меню програми для користувача
    print("""
======================
    Менеджер задач
======================
1. Додати задачу
2. Редагувати задачу
3. Видалити задачу
4. Показати всі задачі
5. Змінити порядок задач
6. Зберегти у файл
7. Відкрити файл
8. Видалити файл
0. Вихід
======================
""")


def main():
    # цикл взаємодії з програмою
    while True:
        try:
            show_menu()
            choice = input("Оберіть дію: ").strip()

            match choice:
                case "1":
                    # вибір дозволяє створити нову задачу
                    title = input("Назва задачі: ")
                    desc = input("Опис: ")
                    manager.add_task(title, desc)
                case "2":
                    # вибір дозволяє відредагувати задачу
                    manager.show_tasks()
                    index = int(input("Яку задачу ви хочете відредагувати: ")) - 1
                    title = input("Нова назва (або Enter, щоб пропустити): ").strip() or None
                    desc = input("Новий опис (або Enter): ").strip() or None
                    status = input("Новий статус (заплановано / виконується / виконано): ").strip() or None
                    manager.edit_task(index, title, desc, status)
                case "3":
                    # вибір дозволяє видалити задачу
                    manager.show_tasks()
                    index = int(input("Яку задачу ви хочете видалити: ")) - 1
                    manager.delete_task(index)
                case "4":
                    # вибір виводить список всіх задач
                    manager.show_tasks()
                case "5":
                    # вибір дозволяє міняти задачі місцями
                    manager.show_tasks()
                    old = int(input("Перемістити задачу №: ")) - 1
                    new = int(input("На позицію №: ")) - 1
                    manager.move_task(old, new)
                case "6":
                    # вибір дозволяє зберегти задачі в конкретний файл
                    filename = input("Назва файлу для збереження (наприклад tasks.json): ")
                    save_to_file(filename, manager.to_dict_list())
                case "7":
                    # вибір дозволяє завантажити задачі з файлу
                    filename = input("Який файл ви хочете відкрити: ")
                    data = load_from_file(filename)
                    manager.from_dict_list(data)
                    print("Задачі підвантажено")
                case "8":
                    # вибір дозволяє видалити файл з задачами
                    filename = input("Який файл ви хочете видалити: ")
                    delete_file(filename)
                case "0":
                    # вибір завершує роботу програми
                    print("Роботу завершено")
                    break
                case _:
                    print("Невідома команда")
        except ValueError:
            print("Введено некоректне число")
            logging.warning("Користувач ввів некоректне число")
        except FileNotFoundError as e:
            print("Файл не знайдено:", e)
            logging.warning(f"Файл не знайдено: {e}")
        except Exception as e:
            print("Сталася неочікувана помилка:", e)
            logging.warning(f"Непередбачена помилка: {e}")



if __name__ == "__main__":
    main()
