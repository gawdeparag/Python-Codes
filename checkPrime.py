import math
number = int(input("Enter a number: "))

def primeNumber(number):
    c = 0
    if (number == 1 or number == 0):
        print("Number is neither Prime nor Composite!")

    for i in range(3, number):
        if(number % i == 0):
            c += 1
            break
        else:
            continue
        
    if (c == 0 or c == 1):
        print("Number is Prime!")
    else:
        print("Number is Composite!")

primeNumber(number)
