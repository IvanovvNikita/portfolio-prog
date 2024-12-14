import sqlite3


def connect(filename: str) -> sqlite3.Connection:
    conn = None

    try:
        conn = sqlite3.connect(filename)
    except sqlite3.DatabaseError:
        print(f'Не удалось подключиться к БД {filename}. Попробуйте снова.')
    return conn


def close(conn: sqlite3.Connection) -> None:
    conn.close()


def read(conn: sqlite3.Connection, table: str) -> None:
    if conn:
        try:
            cursor = conn.cursor()
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
    else:
        print('Ошибка: не удалось подключиться к базе данных.')


def create_table(conn: sqlite3.Connection, table: str, columns: list) -> None:
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
            result = cursor.fetchone()
            if result is None:
                with conn:
                    cursor.execute(f"CREATE TABLE {table} ({','.join(columns)})")
                print(f"Таблица {table} успешно создана.")
            else:
                print(f"Таблица {table} уже существует.")
        except sqlite3.Error as e:
            raise Exception(f"Ошибка при создании таблицы {table}: {e}") from e
    else:
        print('Ошибка: не удалось подключиться к базе данных.')


def insert(conn: sqlite3.Connection, table: str, **kwargs) -> None:
    if conn:
        try:
            cursor = conn.cursor()
            columns = ', '.join(kwargs.keys())
            values = ', '.join(['?' for _ in kwargs.values()])
            insert_query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(insert_query, tuple(kwargs.values()))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении данных {kwargs} в таблицу {table}: {e} ")
    else:
        print('Ошибка: не удалось подключиться к базе данных.')


def update(conn: sqlite3.Connection, table: str, updated_ent: str, condition: str, *args) -> None:
    if conn:
        try:
            cursor = conn.cursor()
            update_query = f"UPDATE {table} SET {updated_ent} WHERE {condition}"
            cursor.execute(update_query, args)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении данных в таблицу {table}: {e}")

    else:
        print('Ошибка: не удалось подключиться к базе данных.')


def delete(conn: sqlite3.Connection, table: str, condition: str, *args) -> None:
    if conn:
        try:
            cursor = conn.cursor()
            delete_query = f"DELETE FROM {table} WHERE {condition}"
            cursor.execute(delete_query, args)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при удалении данных в таблицу {table}: {e}")

    else:
        print('Ошибка: не удалось подключиться к базе данных.')
