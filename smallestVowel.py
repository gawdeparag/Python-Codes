s = input("Enter a string: ")

listOfCharacters = list(s)

vowels = "aAeEiIoOuU"

vowelsFromString = []

for i in listOfCharacters:
    if i in vowels:
        vowelsFromString.append(ord(i))

print("The smallest vowel in above sentence is: {0}".format(chr(min(vowelsFromString))))