# a zip function thate take two or more pairs of values through loop 


lis1=[]
list2=[]


n1=int(input("enter number of values you want in list 1: "))
n2=int(input("enter number of values you want in list 2: "))




print("enter values of list1\n")
for i in range(n1):
    lis1.append(int(input(f"enter value {i+1} : ")))

print("enter values of list2\n")

for j in range(n2):
    list2.append(int(input(f"enter value {j+1} :" )))

print(lis1,list2)
res=[]
for x,y in  zip(lis1,list2):
    res.append(x+y)
print(res)

list3 = [a - b for a, b in zip(lis1, list2)]
print("Subtraction:", list3)

l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5]
l3=[1,3,4,5,6,7,8,9]
res=[]
for x,y,z in zip(l1,l2,l3):
    res.append({x,y,z})
print(res)





rq=l1+l2+l3
print(list(set(rq)))