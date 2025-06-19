arr = [1, 6, 2, 3, 4, 5, 6]
for i in range(len(arr)-1, -1, -1):
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            print(arr[i])
