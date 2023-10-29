from functions import get_todos,write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"): # add + new todo
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)
            

    elif user_action.startswith("show"): # show

        todos = get_todos()

    #list_comprehension : new_todos = [i = i.strip("\n") for i in todos]

        for idx,i in enumerate(todos):
            i = i.strip("\n")
            row = (f"{idx+1}. {i}")
            print(row)

    elif user_action.startswith("edit"): # edit + number of todo to edit
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            
            new_todo = input("Enter new todo:")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except IndexError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"): # complete + number of completed todo
        try:
            number = int(user_action[9:])
            
            todos = get_todos()
            
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)
            
            print(f"The {todo_to_remove} was removed from the toDo list.")
        except:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye")
