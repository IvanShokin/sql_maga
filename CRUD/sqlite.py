


def createUser(cur, data):
    cur.execute("INSERT INTO users(f_name, l_name, gender, age) VALUES(?, ?, ?, ?, ?);", data)
    return print(f'user is created')


def createProject(cur, data):
    cur.execute("INSERT INTO project(title, description, access_level) VALUES(?, ?, ?, ?);", data)
    return print(f'user is created')


def getListUsers(cur):
    return cur.execute("SELECT user FROM users").fetchall()


def getListProjects(cur):
      return cur.execute("SELECT title FROM projects").fetchall()


def getUserInfo(cur, user):
    return cur.execute("SELECT * FROM users WHERE f_name = user").fetch()



def getProjectInfo(cur, project):
    return cur.execute("SELECT * FROM projects WHERE title = project").fetch()



def getUserId(cur, user):
	return cur.execute("SELECT id FROM users WHERE f_name = user").fetch()


def getProjectId(cur, project):
	return cur.execute("SELECT id FROM projects WHERE title = project").fetch()


def getUserProjects(cur, user):
	pass