

def createUser(cur, data):
    cur.execute("INSERT INTO users(f_name, l_name, gender, age) VALUES(?, ?, ?, ?, ?);", data)
    return print(f'user is created')


def createProject(cur, data):
    cur.execute("INSERT INTO project(title, description, access_level) VALUES(?, ?, ?, ?);", data)
    return print(f'user is created')


def getListUsers(cur):
    all_users =  cur.execute("SELECT user FROM users").fetchall()
    return all_users


def getListProjects(cur):
    all_projects =  cur.execute("SELECT title FROM projects").fetchall()
    return all_projects


def getUserInfo(cur, user):
    pass