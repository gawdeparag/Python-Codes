"""A .txt file by the name "stringWrite" gets generated 
with this program and the text which is in the .write() function
gets written in the "stringWrite.txt" file"""

myfile = open("stringWrite.txt", "w")

myfile.write("Hello World! ")
myfile.write("This is File Handling")

myfile.close()
myfile = open("stringWrite.txt", "r")

myfile.close()
print("Done")
