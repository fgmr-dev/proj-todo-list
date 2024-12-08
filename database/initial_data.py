import json
import os
from database.manage import execute_query, table_exists, count_rows


def list_catalogs():
    """Function to list the tables for initial load"""
    data = {}
    if os.path.exists("./data/catalogs.json"):
        with open("./data/catalogs.json", mode="r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        print("No se encontró ningún archivo de datos iniciales.")
    return data


def load_data():
    """Function to load initial data for catalog tables"""
    catalogs = list_catalogs()
    for catalog in catalogs:
        table_name = catalog["table_name"]
        path = catalog["path"]
        if not table_exists(table_name):
            print(f"La tabla '{table_name}' no existe.")
            return

        if count_rows(table_name) == 0:
            # Leer y cargar datos desde JSON
            if os.path.exists(path):
                with open(path, mode="r", encoding="utf-8") as file:
                    data = json.load(file)
                    for row in data:
                        query = f"INSERT INTO {table_name} (description) VALUES (?)"  # noqa: E501
                        execute_query(
                            query,
                            (row["description"],)
                        )
                print(f"Datos iniciales cargados desde JSON: {table_name}")
            else:
                print(f"No se encontró ningún archivo de datos iniciales: {table_name}")
        else:
            print(f"La tabla '{table_name}' ya contiene datos.")


if __name__ == "__main__":
    load_data()
