import json
import os


def save_to_file(filename: str, data: list):
    # Метод зберігає файли в JSON-файл
    # файл відкрито в режимі для запису
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("ERROR saving file:", e)
        return False


def load_from_file(filename: str):
    # Метод завантажує задачі з JSON-файлу
    # Перевірка на існування файлу
    if not os.path.exists(filename):
        print("Файл не знайдено")
        return []
    # Відкриття файлу в режимі читання
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def delete_file(filename: str):
    # Метод видаляє файл в випадку його існування
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return True
        return False
    except Exception as e:
        print("ERROR deleting file:", e)
        return False
