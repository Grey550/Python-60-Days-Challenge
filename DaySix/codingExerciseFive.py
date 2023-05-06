# file = open(r"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\a.txt", 'r')
# a = file.readline()
# print(a)
#
# file = open(r"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\b.txt", 'r')
# b = file.readline()
# print(b)
#
# file = open(r"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\c.txt", 'r')
# c = file.readline()
# print(c)

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(fr"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\{filename}", 'r')
    content = file.read()
    print(content)
