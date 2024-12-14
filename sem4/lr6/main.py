"""
TODO:  
1. Сделать рефакторинг кода таким образом, чтобы объект класса с реализацией подключения к базе данных был синглтоном. Синглтон реализовать или как декоратор для функции, или как декоратор для класса (см. последний конспект лекции)

2. Реализовать параметризованные запросы для 4 видов действий SELECT, INSERT, DELETE, UPDATE
параметризованный запрос или параметризированный запрос / parametrized query    / вместо execute — executemany
# переписать с помощью named style

3. Реализовать в файле user.py класс для пользователя и с помощью механизма свойств осуществить фиксацию значений атрибутов (см. конструктор и структуру таблицы user в БД). Не забыть про базовую проверку атрибутов на осмысленность значений (например, с помощью регулярных выражений).



Иванов Никита 1.1
Лабораторная работа 6.

Работа с SQlite. Классы


"""

if __name__ == "__main__":
    import database 
    import users as u
    from datetime import datetime

    #Конвертируем класс Users в tuple для внесения в бд 
    users = [
        u.User(1, 1.82, 'Maxim', False, datetime.now()).tuple(),
        u.User(2, 1.75, 'Nikita', False, datetime.now()).tuple(),
        u.User(3, 1.78, 'Joe', False, datetime.now()).tuple(),
        u.User(4, 1.65, 'John', False, datetime.now()).tuple(),
        u.User(5, 1.90, 'Anna', False, datetime.now()).tuple(),
        u.User(6, 2.01, 'Kirill', False, datetime.now()).tuple(),
        u.User(7, 1.89, 'Oleg', False, datetime.now()).tuple(),
    ]
    
    db = database.Database(':memory:')
    user_columns = [
        'id INTEGER PRIMARY KEY AUTOINCREMENT',
        'name TEXT',
        'height NUMBER',
        'created TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
        'deleted BOOL DEFAULT \'FALSE\''
    ]
 
    #Создаем таблицу User
    db.create_table('user', user_columns)
    #Попытаемся считать данные таблицы
    db.read('user')
    #Добавим несколько пользователей
    db.insert_many_users('user', users)
    # Считаем данные таблицы
    db.read('user')
    #Удалим пользователя с именем Кирилл по имени
    db.delete('user', "name = 'Kirill'")
    db.read('user')
    #Изменим рост пользователя Олег
    db.update('user',"height = 1.82", "name = 'Oleg'")
    db.read('user')
    
    #Закроем соединение
    db.close()