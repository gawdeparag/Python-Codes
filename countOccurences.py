arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
for i in range(0, len(arr)):
    occurence = arr.count(arr[i])
    print("Element {0} occurs {1} times".format(arr[i], occurence))   

