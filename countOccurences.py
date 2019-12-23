from collections import Counter

arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]

counts = Counter(arr)

for i in counts:
    print("Element {0} occurs {1} times".format(i, counts[i]))
 

