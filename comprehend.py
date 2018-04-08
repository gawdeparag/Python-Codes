n = int(input("Enter the last number: "))

even = [number for number in range(0, n) if number%2 == 0]
print("Even ones: ", even)

odd = [number for number in range(0, n) if number%2 != 0]
print("Odd ones:", odd)