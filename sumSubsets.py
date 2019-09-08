arr = [1, 2, 3, 4, 5, 6]
target = 6
subsetarr = []

for i in range(0, len(arr)):
    if(arr[i] == target):
        subsetarr.append([arr[i], 0])
    for j in range(0, i+1):
        if (arr[i]+arr[j] == target):
            subsetarr.append([arr[i], arr[j]])

print(subsetarr)