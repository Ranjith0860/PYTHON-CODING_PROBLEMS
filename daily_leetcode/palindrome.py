# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

number=int(input("enter number : "))
temparory_num=number
reversed_number=0

while temparory_num > 0:
    remainder=temparory_num % 10
    reversed_number = (reversed_number*10) + remainder
    temparory_num=temparory_num//10
if reversed_number == number:
    print("palindrome")
else:
    print("not a palindrome")
    