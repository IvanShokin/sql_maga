def create(cur, entity, data):
    if entity == 'user':
        cur.execute("INSERT INTO users(user_id, f_name, l_name, gender, age) VALUES(?, ?, ?, ?, ?);", data)
    elif entity == 'project':
        cur.execute("INSERT INTO project(order_id, title, description, access_level) VALUES(?, ?, ?, ?);", data)


def update(cur):
    pass


def read(cur):
    # Информация о сотруднике
    # Информация о проекте
    pass

def delete(cur):
    pass