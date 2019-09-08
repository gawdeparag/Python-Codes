# Initializing dictionary
dic1 = { 'Name' : 'MySQL', 'Server' : 'XAMPP', 'Stack': 'LAMP' }
dic3 = {}
# using copy() to make shallow copy of dictionary
dic3 = dic1.copy()
# printing new dictionary
print ("The new copied dictionary is : ")
print (dic3.items())
dic1.clear()
# printing cleared dictionary
print ("The contents of deleted dictionary is : ")
print (dic3.items())

