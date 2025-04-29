# #first small index =i
# in second loop starts from i+1,len
# if arr[j]<arr[min]
# min=j
# min wii increase repeate the loop

array=[15,24,22,11,44,23,21]
for i in range(len(array)):
    min_index=i
    for j in range (i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
        
    array[i],array[min_index]=array[min_index],array[i]
    print(array)
print(array)