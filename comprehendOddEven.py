"""This program takes a range of numbers as input, starting from 0 
and the last number of this range is taken as user input.
Then, this program prints all the even and odd numbers 
from 0 to the user input number
USING COMPREHEND Property"""

print("Give any number and all the even-odds from 0 to that number will be printed")
n = int(input("Enter the last number: "))

even = [number for number in range(0, n) if number%2 == 0]
print("Even ones: ", even)

odd = [number for number in range(0, n) if number%2 != 0]
print("Odd ones:", odd)