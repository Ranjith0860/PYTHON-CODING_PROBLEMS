# List inputs
list1 = []
list2 = []

n = int(input("Enter number of elements in list1: "))
n2=int(input("Enter number of elements in list2: "))

print("\nEnter elements for List 1:")
for i in range(n):
    list1.append(int(input(f"Element {i+1}: ")))

print("\nEnter elements for List 2:")
for i in range(n2):
    list2.append(int(input(f"Element {i+1}: ")))

# Menu
print("""
Choose an Operation:
1. Pairwise Addition
2. Pairwise Subtraction
3. Pairwise Multiplication
4. Pairwise Division
5. Pairwise Maximum
6. Pairwise Minimum
7. Pairwise Tuples (zip)
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    result = [a + b for a, b in zip(list1, list2)]
    print("Pairwise Addition:", result)

elif choice == 2:
    result = [a - b for a, b in zip(list1, list2)]
    print("Pairwise Subtraction:", result)

elif choice == 3:
    result = [a * b for a, b in zip(list1, list2)]
    print("Pairwise Multiplication:", result)

elif choice == 4:
    result = []
    for a, b in zip(list1, list2):
        if b == 0:
            result.append("Undefined (division by zero)")
        else:
            result.append(a / b)
    print("Pairwise Division:", result)

elif choice == 5:
    result = [max(a, b) for a, b in zip(list1, list2)]
    print("Pairwise Maximum:", result)

elif choice == 6:
    result = [min(a, b) for a, b in zip(list1, list2)]
    print("Pairwise Minimum:", result)

elif choice == 7:
    result = list(zip(list1, list2))
    print("Paired Tuples:", result)

else:
    print("Invalid Choice!")
