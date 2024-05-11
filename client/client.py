import Pyro4

uri = "PYRO:example.server@localhost:9090"
server = Pyro4.Proxy(uri)

server.add_group("Group 1")
server.add_student("John Doe", 1)
server.list_groups()
server.list_students_in_group(1)
server.update_student_name(1, "Jane Doe")
server.delete_student(1)
server.delete_group(1)
