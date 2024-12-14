"""
Иванов Никита 1.1
Лабораторная работа 5.

Работа с SQlite

"""

import app

database = 'database.sqlite'
user_columns = [
    'id INTEGER PRIMARY KEY AUTOINCREMENT',
    'name TEXT',
    'height NUMBER',
    'created TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
    'deleted BOOL DEFAULT \'FALSE\''
]

car_columns = [
    'id INTEGER PRIMARY KEY AUTOINCREMENT',
    'make TEXT NOT NULL',
    'model TEXT NOT NULL',
    'year INTEGER',
    'color TEXT',
    'price REAL NOT NULL',
    'created TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
]

if __name__ == '__main__':

  #Устанавливаем соединение с базой данных
  c = app.connect(database)
  #Создаем таблицу User
  app.create_table(c,'user',user_columns)
  #Попытаемся считать данные таблицы
  app.read(c, 'user')
  #Добавим несколько пользователей
  app.insert(c,'user', name = 'Nikita', height = 1.74)
  app.insert(c,'user', name = 'Kirill', height = 1.5)
  app.insert(c,'user', name = 'Oleg', height = 1.8)
  # Считаем данные таблицы
  app.read(c, 'user')
  #Удалим пользователя с именем Кирилл по имени
  app.delete(c,'user', "name = 'Kirill'")
  app.read(c, 'user')
  #Изменим рост пользователя Олег
  app.update(c,'user',"height = 1.82", "name = 'Oleg'")
  app.read(c, 'user')

  #Создадим таблицу car и добавим в нее значения
  app.create_table(c,'car',car_columns)
  app.insert(c,'car', make = 'GAZ', model = 'Volga', year = 1997,color = 'Black', price = 55000)
  app.insert(c,'car', make = 'Lada', model = 'Largus', year = 2015,color = 'Gray', price = 470000)
  app.read(c, 'car')
  #Изменим цену Волги и удалим Ладу Ларгус по id
  app.update(c,'car', "price = 50000", "id = 1")
  app.delete(c,'car', "id = 2")
  app.read(c, 'car')
  #Закроем соединение
  app.close(c)