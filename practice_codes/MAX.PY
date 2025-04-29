# input_string = input()  # Take input like '1,2,3,4'
# numbers = input_string.split(',')  # Split the string into a list of strings ['1', '2', '3', '4']

# # Convert each string into an integer
# numbers = [int(num) for num in numbers]

# print(numbers) 
# print(max(numbers))
# print(min(numbers)) # This will print the list of integers: [1, 2, 3, 4]



# arr = []  # Initialize an empty list
# n = int(input("Enter the number of elements: "))  # Take the number of inputs

# for i in range(n):
#     num = int(input(f"Enter element {i+1}: "))  # Get input from the user
#     arr.append(num)

# # Initialize max and min with the first element of the array
# max_value = arr[0]
# min_value = arr[0]

# Find max and min
# for num in arr:
    # if num > max_value:
    #     max_value = num
    # if num < min_value:  # Fix the min condition
    #     min_value = num

# print(f"Maximum: {max_value}, Minimum: {min_value}")




# num1=int(input("enter the number of elements"))
# num2=[]
# for i in range(num1):
#     value=int(input(f"element{i}: "))
#     num2.append(value)
# max_value=num2[0]
# for j in num2:
#     if j>max_value:
#         max_value=j
# print(max_value)


try:
    num=int(input("enter a number for range "))
    num2=[]
    for i in range(1,num+1):
        vaule=int(input(f"Element {i}:"))
        num2.append(vaule)
    max_value=num2[0]
    min_value=num2[1]
    for j in num2:
        if max_value<j:
            max_value=j
        if min_value>j:
            min_value=j
    print(f"The max value is:{max_value}")
    print(f"The min_value is:{min_value}")
except ValueError:
    print(f"please Enter an integer :")
