number = int(input("Enter a number: "))

def primeNumber(number):
    c = 1
    if (number == 1 or number == 0):
        print("Number is neither Prime nor Composite!")
        return

    for i in range(3, number):
        if(number % i == 0):
            c = 0
            break
        
    if (c == 1):
        print("Number is Prime!")
    else:
        print("Number is Composite!")

primeNumber(number)
