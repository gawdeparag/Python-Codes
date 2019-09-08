"""
NeoSoft Technical Round Question:

If n = 5, the Pattern expected here is: 
1 2 3 4 5
  2 3 4 5
    3 4 5
      4 5
        5
        4 5
        3 4 5
        2 3 4 5
        1 2 3 4 5
"""
n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(i-1):
        print(" ", end=" ")
    for k in range(i, n+1):
        print(k, end=" ")
    print()

for l in range(n-1):
    for o in range(n-1):
        print(" ", end=" ")
    for m in range(n-l-1, n+1):
        print(m, end=" ")
    print()
