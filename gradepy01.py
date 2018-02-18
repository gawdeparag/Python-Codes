def entry():
    print("Enter your marks")
    m1 = int(input("Marks of Subject 1: "))
    m2 = int(input("Marks of Subject 2: "))
    m3 = int(input("Marks of Subject 3: "))
    m4 = int(input("Marks of Subject 4: "))
    m5 = int(input("Marks of Subject 5: "))
    grade(m1, m2, m3, m4, m5)

def grade(m1, m2, m3, m4, m5):
    sum = m1+m2+m3+m4+m5
    print("Total marks: ", sum)
    avg = sum/5

    if avg >= 74 and avg <= 100:
        if avg == 74:
            avg = avg + 1
        print("Your average is: ", avg)
        print("Result: Distinction")
    elif avg >= 59 and avg <= 73:
        if avg == 59:
            avg = avg + 1
        print("Your average is: ", avg)
        print("Result: First Class")
    elif avg >= 49 and avg <=58:
        if avg == 49:
            avg = avg + 1
        print("Your average is: ", avg)
        print("Result: Second Class")
    elif avg >= 39 and avg <= 48:
        if avg == 39:
            avg = avg + 1
        print("Your Average is: ", avg)
        print("Result: Third Class")
    elif avg > 100:
        print("Invalid operation! Try again!")
    else:
        print("You have failed!")

entry()