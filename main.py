while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:  # reads from a file and doesn't override
                todos = file.readlines()
            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')  # removes line breaks from the list
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("Number of the task you want to edit: "))
            number = number - 1  # used to make sure that the entered number is not viewed as element

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter your new task: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the task to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"{todo_to_remove} was removed from the list"
            print(message)
        case "exit":
            break
        case _:
            print("enter the right data")
print("Bye")

