import math

num = int(input("Enter the minutes: "))


def TimeConvert(num):
    hours = math.floor(num / 60)
    minutes = num % 60
    if(hours > 1):
        print("{0} hours {1} minutes".format(hours, minutes))
    elif(hours == 1):
        print("{0} hour {1} minutes".format(hours, minutes))
    else:
        print("{0} minutes".format(minutes))


TimeConvert(num)
