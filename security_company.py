from CRUD import sqlite
import sqlite3

# NULL — значение NULL
# INTEGER — целое число
# REAL — число с плавающей точкой
# TEXT — текст
# BLOB — бинарное представление крупных объектов, хранящееся в точности с тем, как его ввели


conn = sqlite3.connect('staff.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   f_name TEXT,
   l_name TEXT,
   gender TEXT,
   age INTEGER);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS project(
   order_id INT PRIMARY KEY,
   title TEXT,
   description TEXT,
   access_level INTEGER);
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
	pass

elif command == 2:
	pass

elif command == 3:
	cur.execute("SELECT * FROM users;")
	three_results = cur.fetchmany(3)
	print('\n'.join(three_results))

elif command == 4:
	pass

conn.commit()



