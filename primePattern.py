"""
Here a pattern of 'n' number of lines of prime numbers is expected.
If n = 5, then,
2   3
5   7   11  
13  17  19  23  
29  31  37  41  43  
47  53  59  61  67  71
"""

def primeNumber(number):
    c = 1
    if (number == 1 or number == 0):
        print("Number is neither Prime nor Composite!")
        return

    for i in range(2, number):
        if(number % i == 0):
            c = 0
            break
        
    if (c == 1):
        return True
    else:
        return False

n = int(input("Enter the number of lines: "))

number = 2

for i in range(1, n+1):
    for j in range(i+1):
        while(not primeNumber(number)):
            number += 1
        print(number, end=" ")
        number += 1
    print()
