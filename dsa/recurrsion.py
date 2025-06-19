# # a function calling itself  recuression
# # factorial
def print_num(n):
    if n==0:
        return 0
    print(n)
    print_num(n - 1)
print_num(5)

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))

# def summ(i):
#     if i==0:
#         return  0
#     return i+summ(i-1)
    
# print(summ(5))


# def feb(n):
#     if n==1 : #0 1 1 2 
#         return 0
#     elif n==2:
#         return 1
    
#     return feb(n-1) + feb(n-2)
# for i in range(1,11):
#     print(feb(i),end=" ")





# def factorial(n):#factorial in loop in input  format also
#     if n==0: 
#         return 1
#     return n*factorial(n-1)
# input=int(input("Enter a number:"))
# print(f"the factorial of {input} is {factorial(input)}")

# for i in range(1,input+1):
#     print(f"the factorial of a {i} :{factorial(i),}")



#sum of digits using reciression

# def sum_digits(n):
#     if n==0:
#         return 0
#     return n+sum_digits(n-1)

# for i in range(1,6):
#     print(f"sum of given digits of {i} is  {i} + {sum_digits(i-1)} = {sum_digits(i)}")


def febi(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return n+febi(n-1)

print(febi(5))


















