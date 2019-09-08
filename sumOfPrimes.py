def primeNumber(number):
    c = 1
    if (number == 1 or number == 0 or number < 0):
        c = 1
        return

    for i in range(2, number):
        if(number % i == 0):
            c = 0
            break
        
    if (c == 1):
        return True
    else:
        return False

def sumprimes(l):
    arrayOfPrimes = []
    for i in range(len(l)):
        if(primeNumber(l[i])):
            arrayOfPrimes.append(l[i])
    print(sum(arrayOfPrimes))

sumprimes([3, 3, 1, 13])
sumprimes([2, 4, 6, 9, 11])
sumprimes([-3, 6, 1])