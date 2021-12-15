def createUser(cur, data):
    cur.execute("INSERT INTO user(f_name, l_name, gender, age) VALUES(?, ?, ?, ?);", data)


def createProject(cur, data):
    cur.execute("INSERT INTO project(title, description, access_level) VALUES(?, ?, ?);", data)


def getListUsers(cur):
    return cur.execute("SELECT f_name FROM user").fetchall()


def getListProjects(cur):
    return cur.execute("SELECT title FROM project").fetchall()


def getUserInfo(cur, user):
    return cur.execute(f"SELECT * FROM user WHERE f_name = ?", (user, )).fetchone()


def getProjectInfo(cur, project):
    return cur.execute(f"SELECT * FROM project WHERE title = ?", (project, )).fetchone()


#######################################################################################################################
def getUserId(cur, name):
    return cur.execute(f"SELECT id FROM user WHERE f_name = ?", (name, )).fetchone()


def getUserProjects(cur, project):
    return cur.execute(f"SELECT project_id FROM user_project WHERE user_id = ?", getUserId(cur, project)).fetchall()


def getNameUserProjects(cur, project):
    response = []
    for id in getUserProjects(cur, project):
        response.append(*cur.execute("SELECT title FROM project WHERE id = ?", id).fetchone())
    return response


#######################################################################################################################
def getProjectId(cur, name):
    return cur.execute(f"SELECT id FROM project WHERE title = ?", (name, )).fetchone()


def getProjectUsers(cur, project):
    return cur.execute(f"SELECT user_id FROM user_project WHERE project_id = ?", getProjectId(cur, project)).fetchall()


def getNameProjectUsers(cur, project):
    response = []
    for id in getProjectUsers(cur, project):
        response.append(*cur.execute("SELECT f_name FROM user WHERE id = ?", id).fetchone())
    return response
#######################################################################################################################