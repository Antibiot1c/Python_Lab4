import Pyro4
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    group_id INTEGER PRIMARY KEY,
                    group_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    student_name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY(group_id) REFERENCES groups(group_id))''')
conn.commit()

@Pyro4.expose
class Server:
    def add_group(self, group_name):
        cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group_name,))
        conn.commit()
        return f"Group '{group_name}' added successfully."

    def add_student(self, student_name, group_id):
        cursor.execute('INSERT INTO students (student_name, group_id) VALUES (?, ?)', (student_name, group_id))
        conn.commit()
        return f"Student '{student_name}' added to group {group_id} successfully."


daemon = Pyro4.Daemon()
uri = daemon.register(Server)
print("URI:", uri)

ns = Pyro4.locateNS()
ns.register("example.server", uri)

print("Server is ready.")
daemon.requestLoop()
