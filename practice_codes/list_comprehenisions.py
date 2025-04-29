# lists = (map(int, input("enter number").split(",")))  # Convert input to a list of integers
# updated = [num for num in lists if num % 2 == 0] # Keep only even numbers
# print(updated)



def find_divisible_numbers():
    try:
        # Taking input and splitting by comma
        a, b = map(int, input("Enter two numbers (a,b): ").split(","))

        # Handling division by zero
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return

        print(f"Numbers between 1 and {a} that are divisible by {b}:")
        
        # Loop through numbers from 1 to a and check divisibility
        divisible_numbers = [i for i in range(1, a + 1) if i % b == 0]

        # Print the result
        if divisible_numbers:
            print(*divisible_numbers)
        else:
            print("No numbers found.")

    except ValueError:
        print("Invalid input! Please enter two integers separated by a comma.")

# Calling the function
find_divisible_numbers()

