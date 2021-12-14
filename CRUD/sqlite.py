def createUser(cur, data):
    cur.execute("INSERT INTO users(f_name, l_name, gender, age) VALUES(?, ?, ?, ?);", data)


def createProject(cur, data):
    cur.execute("INSERT INTO project(title, description, access_level) VALUES(?, ?, ?);", data)


def getListUsers(cur):
    return cur.execute("SELECT f_name FROM users").fetchall()


def getListProjects(cur):
    return cur.execute("SELECT title FROM project").fetchall()


def getUserInfo(cur, user):
    return cur.execute(f"SELECT * FROM users WHERE f_name = {user}").fetchone()


def getProjectInfo(cur, project):
    return cur.execute(f"SELECT * FROM project WHERE title = {project}").fetchone()


def getUserId(cur, user):
    return cur.execute(f"SELECT id FROM users WHERE f_name = {user}").fetchone()


def getUserProjects(cur, user):
    param = getUserId(cur, user)
    return cur.execute(f"SELECT project_id FROM user_project WHERE user_id = {param}").fetchAll()


def getProjectId(cur, project):
    return cur.execute(f"SELECT id FROM project WHERE title = {project}").fetchone()


def getProjectUsers(cur, project):
    param = getProjectId(cur, project)
    return cur.execute(f"SELECT user_id FROM user_project WHERE project_id = {param}").fetchAll()
