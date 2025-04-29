# n1=int(input())
# n2=int(input("enter n2"))
# count=0
# for num in range(n1,n2+1):
#   s=str(num)
#   k=set(s)
#   if len(s)==len(k):
#     count+=1
# print(count)



n1 = int(input("enter number"))  # Take a single number as input
count = 0  # Initialize count

# Iterate through numbers from 1 to n1 (inclusive)
# for num in range(1, n1 + 1):
#     s = str(num)  # Convert number to string
#     k = set(s)  # Convert string to a set to remove duplicates
    
#     if len(s) == len(k):  # Check if all digits are unique
#         count += 1  # Increment count if unique

# print(count)  # Print the count of numbers with unique digits


num_range = input()  # Take a single input

# Split input into two numbers
n1, n2 = map(int, num_range.split())

count = 0  # Initialize count

# Iterate through numbers from n1 to n2 (inclusive)
for num in range(n1, n2 + 1):
    s = str(num)  # Convert number to string
    k = set(s)  # Convert string to a set to remove duplicates
    
    if len(s) == len(k):  # Check if all digits are unique
        count += 1  # Increment count if unique

print(count)  # Print the count of numbers with unique digits
