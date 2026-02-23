# TEXT ANALYSIS USING FUNCTIONS

# 1. count words
def count_words(text):
    words = text.split()
    return len(words)

# 2. count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# 3. count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

# 4. reverse text
def reverse_text(text):
    return text[::-1]

# 5. palindrome check (ignore case & spaces)
def is_palindrome(text):
    clean = text.replace(" ", "").lower()
    return clean == clean[::-1]

# 6. remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

# 7. word frequency dictionary
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# 8. longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest, len(longest)


# 9. main function
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    # palindrome result format
    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    # longest word display
    word, length = longest_word(text)
    print("Longest word:", word, f"({length} letters)")

    # word frequency display in sample style
    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    first = True
    for k, v in freq.items():
        if not first:
            print(",", end=" ")
        print(f"{k}: {v}", end="")
        first = False
    print()


# PROGRAM
user_text = input("Enter text: ")
analyze_text(user_text)