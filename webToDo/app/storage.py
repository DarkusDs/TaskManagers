import json
import os
from typing import List


def save_to_file(filename: str, data: List[dict]) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print("ERROR saving file:", e)
        return False


def load_from_file(filename: str) -> List[dict]:
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def delete_file(filename: str) -> bool:
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return True
        return False
    except Exception as e:
        print("ERROR deleting file:", e)
        return False
