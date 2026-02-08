n = 10   # how many terms you want

a, b = 0, 1
print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
