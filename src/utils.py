import json
import os


def load_data():
    """
    Функция, которая загружает данные из json-файла
    """
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "../data/products.json")

    with open(file_path) as file:
        data = json.load(file)

    return data
