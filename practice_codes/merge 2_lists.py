list1=[1,2,3,4]
list2=[4,3,4,5]
list3=[]
for x in (list1+list2):
    list3.append(x)
print(list3)

for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)


for uniq in (list1+list2):
    if uniq not in list3:
        list3.append(uniq)
print(f"unique elements{list3}")

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(list1,list2)
print("Pairwise Addition:", list3)