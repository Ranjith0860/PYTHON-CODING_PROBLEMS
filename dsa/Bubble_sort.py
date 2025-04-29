array = [7, 2, 9, 4, 1, 5, 3]

for i in range(len(array)):
    for j in range(len(array)-i-1):#9-0-1=8-->0,7
        if array[j]>array[j+1]:
            array[j], array[j + 1] = array[j + 1], array[j] 
    print(array)