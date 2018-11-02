import math

num = int(input("Enter the minutes: "))


def TimeConvert(num):
    hours = math.floor(num / 60)
    minutes = num % 60
    print(hours, ":", minutes)


TimeConvert(num)
