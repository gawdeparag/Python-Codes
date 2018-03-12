while True:
    print('1.Addition') 
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Remainder')
    print('6.Exit')
    option = int(input("Enter your option: "))
    if option == 6:
        break
    elif option == 1:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        print("Addition is ",(a+b))
    elif option == 2:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        print("Subtraction is ",(a-b))
    elif option == 3:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        print("Multiplication is ",(a*b))
    elif option == 4:
        try:
            a = int(input("Enter your first number: "))
            b = int(input("Enter your second number: "))
            c = a/b
        except ZeroDivisionError:
            print("You can't divide by zero! Try Again Later")
        else:
            print("Division is ",(a/b))
    elif option == 5:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        print("Remainder is ",(a%b))
    else:
        print("Invalid option! Try Again!!")
