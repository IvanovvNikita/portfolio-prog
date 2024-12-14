import sqlite3


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Database:

    def __init__(self, filename: str):
        try:
            self.conn = sqlite3.connect(filename)
        except sqlite3.DatabaseError as e:
            # Возвращаем ошибку, чтобы избежать создания класса
            raise Exception(
                f'Не удалось подключиться к БД {filename}. Попробуйте снова.'
            ) from e

    def close(self) -> None:
        if self.conn is not None:
            self.conn.close()

    def execute_query(self, query: str, params: tuple = ()) -> list:
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f'Возникла ошибка: {e}')
            return []

    def read(self, table: str) -> None:
        try:
            cursor = self.conn.cursor()
            crud_read_str = f"SELECT * FROM {table}"
            cursor.execute(crud_read_str)
        except sqlite3.Error as e:
            print(f'Возникла ошибка: {e}')
        else:
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print(f'Таблица {table} пустая.')
        print()

    def create_table(self, table: str, columns: list) -> None:
        try:
            self.execute_query(
                f"CREATE TABLE IF NOT EXISTS {table} ({','.join(columns)})")
            print(f"Таблица {table} успешно создана.")
        except sqlite3.Error as e:
            raise Exception(f"Ошибка при создании таблицы {table}: {e}") from e

    def select(self,
               table: str,
               columns: list = ('*', ),
               condition: str = '',
               params: tuple = ()) -> list:
        cols_str = ', '.join(columns)
        query = f"SELECT {cols_str} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query, params)

    def insert(self, table: str, data: dict) -> None:
        keys = ', '.join(data.keys())
        values = ', '.join([':' + key for key in data.keys()])
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        self.execute_query(query, data)

    def insert_many_users(self, table: str, data: dict) -> None:
        query = f"INSERT INTO {table} (id, name, height, deleted, created) VALUES (:id, :name, :height, :deleted, :created)"
        self.conn.executemany(query, data)
        
    def update(self, table: str, updated_ent: str, condition: str, *args) -> None:
        try:
            update_query = f"UPDATE {table} SET {updated_ent} WHERE {condition}"
            self.execute_query(update_query, args)
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении данных в таблицу {table}: {e}")

    def delete(self, table: str, condition: str, params: tuple = ()) -> None:
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query, params)
