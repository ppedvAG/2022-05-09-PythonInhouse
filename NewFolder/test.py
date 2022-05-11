import sqlite3
from sqlite3 import Error

def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn

def create_table(connection):
    c = connection.cursor()
    c.execute("Create Table if not exists projects(project_id INTEGER Primary KEY, project_name text not null)")
    c.execute("Create Table if not exists tasks(task_id INTEGER Primary KEY, task_name text not null, completed Integer not null, project_id Integer not null, Foreign Key (project_id) References projects (project_id) On update cascade on delete cascade)")
    connection.commit() # Ist wichtig, da sonst die Transaktionen nicht gespeichert werden

def insert_project(connection):
    project_name = input("Wie heißt das Projekt?\n")
    c = connection.cursor()
    project_id = len(c.execute("Select * from projects").fetchall())
    c.execute("Insert into projects values(?, ?)", (project_id ,project_name))
    connection.commit()

def insert_task(connection):
    c = connection.cursor()
    task_id = len(c.execute("Select * from tasks").fetchall())
    project_id = int(input("Zu welchem projekt gehört die Aufgabe?\n"))
    task_name = input("Wie heißt die Aufgabe?\n")
    c.execute("Insert into tasks values(?,?,?,?)", (task_id, task_name, 0, project_id))
    connection.commit()

if __name__ == "__main__":
    conn = create_connection("test.db")
    create_table(conn)
    insert_project(conn)
    insert_task(conn)
    conn.close()
    

# Major.Minor.Patch
# 