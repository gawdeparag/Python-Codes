import random

option = str("y")
print("---Let's Roll the Dice---")
while (True):
    print (random.randint(1, 6))
    option = input("Want to still continue rolling dice? ")
    if(option == "n" or option == "N"):
        break
    elif(option == "Y"):
        continue
    else:
        continue
    