arr = [0, 1, 2, 3, 4, 5, 6]
target = 36
subsetarr = []

for i in range(0, len(arr)):
    for j in range(0, i+1):
        if (arr[i]*arr[j] == target):
            subsetarr.append([arr[i], arr[j]])

print(subsetarr)