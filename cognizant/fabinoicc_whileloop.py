# a b 0,1assign  
# runs on some condition i.e  count=0
# print a
# c= a+b
# a=b
# b=c
#count increase a=0
# b=1
# 0,c=1,a=1,b=1

# 
n=10
a,b=0,1
count =0
while count<n:
    print(a,end=" ")
    c=a+b
    a,b=b,c
    count+=1

