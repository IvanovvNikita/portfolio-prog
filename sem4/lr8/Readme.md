# Лабораторная работа №8: Работа с ORM Orator. Реализация CRUD-операций

### Цель работы:  
Изучение работы с ORM (Object-Relational Mapping) на примере библиотеки **Orator** для Python. Реализация базовых операций работы с базой данных: создание, чтение, обновление и удаление (CRUD).  

---

## Описание решения:  

#### 1. Настройка ORM Orator:  
- Настроен конфигурационный файл для подключения к базе данных `sqlite`.  
- Подключение к БД осуществляется через объект `DatabaseManager`.  
- Создана таблица `users` с колонками:
  - `id` — первичный ключ (автоинкремент).  
  - `name` — строковое поле для имени пользователя.  
  - `height` — вещественное число, описывающее рост пользователя.  

Код настройки базы данных:  
```python
from orator import DatabaseManager, Model, Schema

config = {
    'default': 'sqlite',
    'sqlite': {
        'driver': 'sqlite',
        'database': 'ormdb.db'
    },
}

db = DatabaseManager(config)
schema = Schema(db)
Model.set_connection_resolver(db)

if not schema.has_table('users'):
    with schema.create('users') as table:
        table.increments('id')
        table.string('name')
        table.float('height')
```
---

#### 2. Реализация модели `User`:  
- Модель наследуется от класса `Model` библиотеки Orator.  
- Указаны основные параметры:  
  - Таблица, с которой связана модель (`__table__ = 'users'`).  
  - Отключены временные метки (`__timestamps__ = False`).  
- Методы класса:  
  - **`print_all_users()`** — вывод всех пользователей из таблицы.  
  - **`find_by_name(name)`** — поиск пользователей по имени.  
  - **`create(name, height)`** — добавление нового пользователя.  
  - **`update(name=None, height=None)`** — обновление данных пользователя.  

Код модели `User`:  
```python
from orator import Model

class User(Model):
    __table__ = 'users'
    __timestamps__ = False

    @classmethod
    def print_all_users(cls):
        res = cls.all()
        for _r in res:
            print(f"{_r.id}  {_r.name}  {_r.height}")

    @classmethod
    def find_by_name(cls, name):
        return cls.where('name', '=', name).get()

    @classmethod
    def create(cls, name, height):
        new_u = cls()
        new_u.name = name
        new_u.height = height
        new_u.save()
        return new_u

    def update(self, name=None, height=None):
        if name:
            self.name = name
        if height:
            self.height = height
        self.save()
```

### Вывод:  
В ходе выполнения лабораторной работы:  
- Реализована работа с базой данных через ORM Orator.  
- Осуществлена настройка подключения к БД SQLite.  
- Реализованы основные CRUD-операции (создание, чтение, обновление, удаление).   
