def armstrong(n):
    temp = n
    sum = 0
    while temp != 0:
        remainder = temp % 10
        sum = sum + remainder ** 3
        temp = temp / 10

    if n == sum:
        print("It's an Armstrong number!")
    else:
        print("It's not an Armstrong number!")

n = int(input("Enter the number you want to check for: "))
armstrong(n)
