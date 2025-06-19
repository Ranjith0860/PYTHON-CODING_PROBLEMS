n = int(input("enter num of words"))
for i in range(n):
    word = input("enter words")
    if len(word) > 10:
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        print(f"{i} WORD = {abbreviation}")
    else:
        print(word)
