import imp
import sqlite3 as sql
from sqlite3 import Error

from matplotlib.pyplot import connect

# Als erstes muss die Verbindung zur Datenbank hergestellt werden

def create_connection(dbName):
    conn = None
    try:
        conn = sql.connect(dbName)
    except Error as e:
        print(e)
    return conn

def create_table(connection):
    c = connection.cursor()
    c.execute("Create Table if not exists users(userId integer primary key, username text not null)")
    connection.commit()   
    
def insert_user(connection):
    c = connection.cursor()
    userId = len(c.execute("Select * from users").fetchall()) + 1
    # fetchall() => GIbt alle Ergebnisse als Liste zurück
    # fetchone() => GIbt ein Ergebniss zurück und schreitet immer weiter
    # fetchmany(anzahl) => Gibt bestimmt viele Einträge zurück
    userName = input("Wie heißt der User?")
    c.execute("insert into users values(?, ?)",(userId, userName))
    # Bei sqlite3 müssen die Werte als Tupel übergeben werden, das Tupel muss aus so vielen Elementen bestehen
    # wie fragezeichen in der Values Klammer stehen
    connection.commit()

def get_user(connection):
    c = connection.cursor()
    userName = input("Wie heißt der gesuchte User?\n")
    c.execute("Select * from users where username like ?", (userName,))
    user = c.fetchone()
    print(user)
    
def get_all_users(connection):
    c = connection.cursor()
    c.execute("Select * from users")
    users = c.fetchall()
    print(users)

if __name__ == "__main__":
    dbName = input("Wie heißt die Datenbank?\n")
    dbName += ".db"
    conn = create_connection(dbName)
    # create_table(conn)
    # insert_user(conn)
    # get_user(conn)
    get_all_users(conn)
    conn.close()