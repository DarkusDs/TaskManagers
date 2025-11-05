import json
import os
from typing import List


def save_to_file(filename: str, data: List[dict]) -> bool:
    # Метод зберігає файли в JSON-файл
    # файл відкрито в режимі для запису
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("ERROR saving file:", e)
        return False


def load_from_file(filename: str) -> List[dict]:
    # Метод завантажує задачі з JSON-файлу
    # Перевірка на існування файлу
    if not os.path.exists(filename):
        return []
    # Відкриття файлу в режимі читання
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def delete_file(filename: str) -> bool:
    # Метод видаляє файл в випадку його існування
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return True
        return False
    except Exception as e:
        print("ERROR deleting file:", e)
        return False
