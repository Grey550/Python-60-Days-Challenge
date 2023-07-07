while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]  # extracts all the characters starting from index 4

        with open('todos.txt', 'r') as file:  # reads from a file and doesn't override
            todos = file.readlines()
        todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # removes line breaks from the list
            row = f"{index + 1}-{item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1  # makes sure that the entered number is not viewed as element

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter your new task: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif "complete" in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip()
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"{todo_to_remove} was removed from the list"
        print(message)
    elif "exit" in user_action:
        break
    else:
        print("Command not valid")

print("Bye")

