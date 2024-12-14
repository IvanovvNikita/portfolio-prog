from orator import DatabaseManager, Model, Schema
from User import User

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

if __name__ == '__main__':

    # Создание таблицы, если она еще не создана
    if not schema.has_table('users'):
        with schema.create('users') as table:
            table.increments('id')
            table.string('name')
            table.float('height')
    #Изначльные данные для базы данных
    new_u = User.create('Nikita', 1.72)
    new_u = User.create('Maxim', 1.75)
    new_u = User.create('Petr', 2.03)
    
    print('Изначальные данные:')       
    User.print_all_users()
    
    #Сreate
    u4 = User.find(4)
    print('Добавление пользователя')
    new_u = User.create('Kirill', 1.6)
    User.print_all_users()

    #Update 
    u4 = User.find(4)
    print('Обновление данных пользователя')
    u4.update(height = 1.65)
    User.print_all_users()
    
    #Delete
    print('Удаление пользователя')
    u4 = User.find(4)
    u4.delete()
    User.print_all_users()

    print('Добавим несколько пользовтелей с именем Кирилл')
    new_u = User.create('Kirill', 1.6)
    new_u = User.create('Kirill', 1.61)
    new_u = User.create('Kirill', 1.62)
    new_u = User.create('Kirill', 1.63)
    User.print_all_users()
    
    #Поиск по имени
    users_name_kirill = User.find_by_name('Kirill')
    print('Удалим всех пользователей с именем Кирилл')
    for user in users_name_kirill:
        user.delete()
    User.print_all_users()