country = input("Which country are you from.? ")
country = country.capitalize()

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")
