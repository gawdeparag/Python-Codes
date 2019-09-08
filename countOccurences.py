arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]

for i in range(0, len(arr)):
    counter = 0
    for j in range(0, i+1):
        if(arr[i] == arr[j]):
            counter += 1      
    print("Element {0} occurs {1} times".format(arr[i], counter))
