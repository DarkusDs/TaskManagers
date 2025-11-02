from models import TaskManager
from storage import save_to_file, load_from_file, delete_file

manager = TaskManager()


def show_menu():
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
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            title = input("Назва задачі: ")
            desc = input("Опис: ")
            manager.add_task(title, desc)
        elif choice == "2":
            manager.show_tasks()
            index = int(input("Яку задачу ви хочете відредагувати: ")) - 1
            title = input("Нова назва (або Enter, щоб пропустити): ").strip() or None
            desc = input("Новий опис (або Enter): ").strip() or None
            status = input("Новий статус (заплановано / виконується / виконано): ").strip() or None
            manager.edit_task(index, title, desc, status)
        elif choice == "3":
            manager.show_tasks()
            index = int(input("Яку задачу ви хочете видалити: ")) - 1
            manager.delete_task(index)
        elif choice == "4":
            manager.show_tasks()
        elif choice == "5":
            manager.show_tasks()
            old = int(input("Перемістити задачу №: ")) - 1
            new = int(input("На позицію №: ")) - 1
            manager.move_task(old, new)
        elif choice == "6":
            filename = input("Назва файлу для збереження (наприклад tasks.json): ")
            save_to_file(filename, manager.to_dict_list())
        elif choice == "7":
            filename = input("Який файл ви хочете відкрити: ")
            data = load_from_file(filename)
            manager.from_dict_list(data)
            print("Задачі підвантажено")
        elif choice == "8":
            filename = input("Який файл ви хочете видалити: ")
            delete_file(filename)
        elif choice == "0":
            print("Роботу завершено")
            break
        else:
            print("Невідома команда")


if __name__ == "__main__":
    main()
