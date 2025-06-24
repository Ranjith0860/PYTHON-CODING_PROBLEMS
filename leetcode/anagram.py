def is_anagram(str1, str2):
    # Clean the strings: remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count characters
    count = {}

    # Count characters in str1
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Subtract character counts using str2
    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            # Character in str2 not in str1
            return False

    # Check if all counts are zero
    for value in count.values():
        if value != 0:
            return False

    return True
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if is_anagram(word1, word2):
    print("✅ The words are anagrams.")
else:
    print("❌ The words are not anagrams.")
