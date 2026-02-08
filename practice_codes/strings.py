#palindrome
# list1 = [10, 20, 30, 40, 50]
# list2 = [20, 40]

# for num in list2:
#     if num in list1:
#         list1.remove(num)

# print(list1)  # Output: [10, 30, 50]
 
# reverse of a string all methods

string="ranjith kumar"
for i in range (len(string)-1,-1,-1):
    print(string[i],end=" ")

# reversed =string[::-1]
# z=list(reversed )


# print(z)

# for j in z:
#     print(j,end="")

# rev="".join(reversed(string))
# print(rev)



# st2=""
# for char in string:
#     st2=char+st2  #r+"",a+"r",n+a+r......
# print(st2)


# s = "Python"
# reversed_s = ""
# i = len(s) - 1  # Start from last index
# while i >= 0:
#     reversed_s += s[i]  # Add characters in reverse order
#     i -= 1  # Move to the previous character
# print(reversed_s)  # Output: "nohtyP"


#recurression
# def reverse_string(s):
#     if len(s) == 0:   # Base case: Stop when string is empty
#         return s
#     return s[-1] + reverse_string(s[:-1])  # Recursive case: Reverse string
