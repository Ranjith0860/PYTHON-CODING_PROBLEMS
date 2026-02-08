st1 = input("Enter string1: ")
st2 = input("Enter string2: ")

dictt = dict()

for i in st1:
    dictt[i] = dictt.get(i, 0) + 1

for j in st2:
    if j in dictt:
        dictt[j] -= 1
    else:
        print("Not an anagram")
        exit()

# Final check
for value in dictt.values():
    if value != 0:
        print("Not an anagram")
        break
else:
    print("True - The strings are anagrams")



# st1 = "banana"
# dictt = {}

# for i in st1:
#     dictt[i] = dictt.get(i, 0) + 1

# for key, value in dictt.items():
#     print(f"{key}: {value}")
