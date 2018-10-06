n = int(input("Enter a number from where you wish to start: "))
for i in range(0, 5):
    for j in range(0, i+1):
        print(n, end=" ")
        n = n + 1
    print()
