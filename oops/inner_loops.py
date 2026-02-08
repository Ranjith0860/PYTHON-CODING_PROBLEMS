name  = list(map(int, input("enter list 1 by space: ").split()))
name2 = list(map(int, input("enter list 2 by space: ").split()))

matched = []
unmatched_1 = []
unmatched_2 = []

for a, b in zip(name, name2):
    if a == b:
        matched.append(a)
    else:
        unmatched_1.append(a)
        unmatched_2.append(b)

print(f"matched numbers are {matched}")
print(f"unmatched numbers in list 1 are {unmatched_1}")
print(f"unmatched numbers in list 2 are {unmatched_2}")


