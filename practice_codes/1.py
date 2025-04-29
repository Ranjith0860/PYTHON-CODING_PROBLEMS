# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()
# # for k in range(5-i):
# #     print("*",end=" ")
# # print()
# a, b, c = input("Enter three values separated by spaces: ").split()
# print(a,b,c)
# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a>b and a<c) or (a<b and a>c):
        print(a)
    elif (b>a and b<c) or (b<a and b>c):
        print(b)
    else:
       print(c)