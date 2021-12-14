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
   id INT PRIMARY KEY,
   f_name TEXT,
   l_name TEXT,
   gender TEXT,
   age INTEGER,);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS project(
   id INT PRIMARY KEY,
   title TEXT,
   description TEXT,
   access_level INTEGER,);
""")

cur.execute("""CREATE TABLE users_project
   user_id  INT,
   project_id INT,
   FOREIGN KEY (user_id) REFERENCES users(id)
   FOREIGN KEY (project_id) REFERENCES project(id));
""")

command = int(input('''
        1 - Добавить сотрудника
        2 - Создать проект
        3 - Поулучить список сотрудников
        4 - Получить список проектов
        5 - Информация о сотруднике
        6 - Информация о проекте
        7 - Сотрудники по должности
'''))

if command == 1:
    data = tuple(input('Введите Имя, Фамилию, Пол, Возраст через пробел: ').split())
    createUser(cur, data)
    print(f'Сотрудник {data[0]} добавлен')
elif command == 2:
    title = input('Введите название проекта: ')
    description = input('Введите описание проекта: ')
    createProject(cur, (title, description))
    print(f'Проект {title} создан')
elif command == 3:
    for user in getListUsers(cur):
        print(*user)
elif command == 4:
    for user in getListProjects(cur):
        print(*user)
elif command == 5:


conn.commit()
