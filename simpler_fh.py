myfile = open("Stringcount.txt", "w")

myfile.write("Hello World!")
myfile.write("This is File Handling")

myfile.close()

myfile = open("Stringcount.txt", "r")

myfile.close()
