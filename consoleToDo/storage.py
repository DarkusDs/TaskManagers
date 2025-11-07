import json
import logging
import os


def save_to_file(filename: str, data: list):
    # Метод зберігає файли в JSON-файл
    # файл відкрито в режимі для запису
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Задачі успішно збережено у файл: {filename}")
        return True
    except Exception as e:
        print("ERROR saving file:", e)
        logging.error(f"Помилка при збереженні у файл {filename}: {e}")
        return False


def load_from_file(filename: str):
    # Метод завантажує задачі з JSON-файлу
    # Перевірка на існування файлу
    if not os.path.exists(filename):
        print("Файл не знайдено")
        logging.warning(f"Спроба завантаження неіснуючого файлу: {filename}")
        return []
    # Відкриття файлу в режимі читання
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info(f"Успішно завантажено файл {filename}")
            return data
    except Exception as e:
        print("ERROR loading file:", e)
        logging.error(f"Помилка при читанні файлу {filename}: {e}")
        return []



def delete_file(filename: str):
    # Метод видаляє файл в випадку його існування
    try:
        if os.path.exists(filename):
            os.remove(filename)
            logging.info(f"Видалено файл {filename}")
            return True
        else:
            logging.warning(f"Спроба видалити неіснуючий файл")
            return False
    except Exception as e:
        print("ERROR deleting file:", e)
        logging.error(f"Помилка при видаленні файлу {filename}: {e}")
        return False
