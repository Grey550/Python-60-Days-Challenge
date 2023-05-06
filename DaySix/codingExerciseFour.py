# contents = ["Hello", "Hello", "Hello"]
filenames = ["text_1.txt", "text_2.txt", "text_3.txt"]

for filenames in filenames:
    file = open(fr"C:\Users\Angie\OneDrive\Documents\ALX Learning Materials\Python\tests\{filenames}", 'w')
    file.write("Hello Hi")
    file.close()
