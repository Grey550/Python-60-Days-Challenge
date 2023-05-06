member = input("Add a new member: ")

file = open(r"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\members.txt", 'r')
old_members = file.readlines()
file.close()

old_members.append(member + "\n")

file = open(r"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\members.txt", 'w')
old_members = file.writelines(old_members)
file.close()

