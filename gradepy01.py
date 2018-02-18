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
    elif condition:
        
    else:
        print("You have failed!")

entry()