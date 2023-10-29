def get_todos(filepath="files/todos.txt"):

    """Read the text file and return the list of to-do items"""

    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="files/todos.txt"):

    """ Write the to-do items in the text file """
    
    with open(filepath, "w") as file:
            file.writelines(todos_arg)

print("Hello from functions")
