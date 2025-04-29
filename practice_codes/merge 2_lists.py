list1=[1,2,3,4]
list2=[4,3,4,5]
list3=[]
for i in range(len(list1)):
    list3.append(list1[i])
    for j in list2:
        list3.append(list2[i])
print(list3)