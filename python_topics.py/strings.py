import string

def text_analyzer(text):
    # Removing punctuation
    text_clean = text.translate(str.maketrans('', '', string.punctuation))

    # Basic counts
    total_chars = len(text)
    total_chars_nospace = len(text.replace(" ", ""))
    words = text_clean.lower().split()
    total_words = len(words)
    sentences = text.count('.') + text.count('!') + text.count('?')

    # Vowels and consonants count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in text if ch in vowels)
    consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)

    # Most frequent word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    most_frequent = max(word_freq, key=word_freq.get)

    # Palindromes
    palindromes = [word for word in words if word == word[::-1] and len(word) > 2]

    # Display results
    print("\n📊 Text Analysis Result:")
    print(f"Total characters (with spaces): {total_chars}")
    print(f"Total characters (without spaces): {total_chars_nospace}")
    print(f"Total words: {total_words}")
    print(f"Total sentences: {sentences}")
    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
    print(f"Most frequent word: '{most_frequent}' ({word_freq[most_frequent]} times)")
    print(f"Palindrome words: {palindromes if palindromes else 'None'}")

# Main Program
if __name__ == "__main__":
    user_input = input("Enter a paragraph:\n")
    text_analyzer(user_input)
