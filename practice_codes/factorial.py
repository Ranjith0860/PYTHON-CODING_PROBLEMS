def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

k = int(input("Enter a number: "))
print("Factorial is:", fact(k))
