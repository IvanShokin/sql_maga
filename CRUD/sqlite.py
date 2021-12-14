def createUser(cur, data):
    cur.execute("INSERT INTO users(f_name, l_name, gender, age) VALUES(?, ?, ?, ?);", data)


def createProject(cur, data):
    cur.execute("INSERT INTO project(title, description, access_level) VALUES(?, ?, ?);", data)


def getListUsers(cur):
    return cur.execute("SELECT f_name FROM users").fetchall()


def getListProjects(cur):
    return cur.execute("SELECT title FROM project").fetchall()


def getUserInfo(cur, user):
    return cur.execute(f"SELECT * FROM users WHERE f_name = {user}").fetch()


def getProjectInfo(cur, project):
    return cur.execute(f"SELECT * FROM project WHERE title = {project}").fetch()


def getUserId(cur, user):
    return cur.execute(f"SELECT id FROM users WHERE f_name = {user}").fetch()


def getUserProjects(cur, user):
    user_id = getUserId(cur, user)
    return cur.execute(f"SELECT project_id FROM user_project WHERE user_id = {user_id}").fetchAll()


def getProjectId(cur, project):
    return cur.execute(f"SELECT id FROM project WHERE title = {project}").fetch()


def getProjectUsers(cur, project):
    project_id = getProjectId(cur, project)
    return cur.execute(f"SELECT user_id FROM user_project WHERE project_id = {project_id}").fetchAll()
