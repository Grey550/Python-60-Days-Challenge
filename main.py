
while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')  # reads from a file and doesn't override
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')  # saves/writes objects in a file
            file.writelines(todos)
            file.close()
        case "show":
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Number of the task you want to edit: "))
            number = number - 1  # used to make sure that the entered number is not viewed as element
            new_todo = input("Enter your new task: ")
            todos[number] = new_todo
        case "exit":
            break
        case "complete":
            number = int(input("Number of the task to complete: "))
            todos.pop(number - 1)
        case _:
            print("enter the right data")
print("Bye")

