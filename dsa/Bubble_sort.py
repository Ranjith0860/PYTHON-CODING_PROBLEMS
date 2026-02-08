def bubble(array):

    

    for i in range(len(array)):
        for j in range(len(array)-i-1):#9-0-1=8-->0,7
            if array[j]>array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j] 
        return array
array =list(map(int,input("enter array list with space").split()))
print(bubble(array))


# def dub(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#              return True
#         seen.add(num)
        
#     return False
    
# nums=list(map(int,input("enter array list with space for dublicates").split()))
# print(f" the give array consist of dubilcates: {dub(nums)}")



# array=list(map(int,input("enter array list with space").split()))


# for i in range(len(array)):
#     for j in range(len(array)-1-i):
#         if array[j]>array[j+1]:
#             array[j],array[j+1]=array[j+1],array[j]
#     print(array)
