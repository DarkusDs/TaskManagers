import json
import os


def save_to_file(filename: str, data: list):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Задачі збережено у файл: {filename}")


def load_from_file(filename: str):
    if not os.path.exists(filename):
        print("Файл не знайдено")
        return []
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def delete_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} видалено")
    else:
        print("Файл не знайдено")
