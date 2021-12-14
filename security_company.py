from CRUD.sqlite import *
import sqlite3

# NULL — значение NULL
# INTEGER — целое число
# REAL — число с плавающей точкой
# TEXT — текст
# BLOB — бинарное представление крупных объектов, хранящееся в точности с тем, как его ввели


conn = sqlite3.connect('staff.db')
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   f_name TEXT,
   l_name TEXT,
   gender TEXT,
   age INTEGER);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS project(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   title TEXT,
   description TEXT,
   access_level INTEGER);
""")

cur.execute("""CREATE TABLE users_project(
   user_id  INT,
   project_id INT,
   FOREIGN KEY (user_id) REFERENCES users(id)
   FOREIGN KEY (project_id) REFERENCES project(id));
""")

while True:
    command = int(input('''
    1 - Добавить сотрудника
    2 - Создать проект
    3 - Поулучить список сотрудников
    4 - Получить список проектов
    5 - Информация о сотруднике
    6 - Информация о проекте
    7 - Проекты сотрудника
    8 - Сотрудники проекта
    9 - Выйти
    '''))

    if command == 1:
        data = tuple(input('Введите Имя, Фамилию, Пол, Возраст через пробел: ').split())
        createUser(cur, data)
        print(f'Сотрудник {data[0]} добавлен')
    elif command == 2:
        title = input('Введите название проекта: ')
        description = input('Введите описание проекта: ')
        lvl = int(input('Уровень доступа: '))
        createProject(cur, (title, description, lvl))
        print(f'Проект {title} создан')
    elif command == 3:
        for user in getListUsers(cur):
            print(*user)
    elif command == 4:
        for user in getListProjects(cur):
            print(*user)
    elif command == 5:
        name = input('Введите имя: ')
        print(*getUserInfo(cur, name))
    elif command == 6:
        title = input('Введите название проекта: ')
        print(*getProjectInfo(cur, title))
    elif command == 7:
        name = input('Введите имя: ')
        print(getUserProjects(cur, name))
    elif command == 8:
        title = input('Введите название проекта: ')
        print(getProjectUsers(cur, title))
    elif command == 9:
        break

    conn.commit()
