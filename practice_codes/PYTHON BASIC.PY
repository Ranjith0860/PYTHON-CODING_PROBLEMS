def add(x=None,y=None):
    if x==None:
        x=int(input())
    if y==None:
        y=int(input())
    # return x+y
    return x-(-y)
res=add()
print(f"sum of x and y:{res}")
res1=add(9,10)
print(f"add of x,y:{res1}")


# usage of print statement in functions
def sum_of_two_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")  # Printing inside the function
    return result

# Call the function
sum_of_two_numbers(3, 5)

# example 2
def sum_of_two_numbers(num1, num2):
    return num1 + num2  # Only returning the result, no print inside

# Capture the result outside and print it
result = sum_of_two_numbers(10, 20)
print(f"The sum is: {result}")  # Printing outside the function

# maximum of 2 digits
def max_of_two_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Example usage
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = max_of_two_numbers(number1, number2)
print(f"The maximum of {number1} and {number2} is: {result}")

    

