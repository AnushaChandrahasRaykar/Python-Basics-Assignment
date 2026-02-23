# String Manipulator Program

# taking sentence from user
sentence = input("Enter a sentence: ")

# original sentence
print("Original:", sentence)

# characters with spaces
print("Characters (with spaces):", len(sentence))

# characters without spaces
no_space = sentence.replace(" ", "")
print("Characters (without spaces):", len(no_space))

# total words
words = sentence.split()
print("Words:", len(words))

# uppercase
print("UPPERCASE:", sentence.upper())

# lowercase
print("lowercase:", sentence.lower())

# title case
print("Title Case:", sentence.title())

# first word
print("First word:", words[0])

# last word
print("Last word:", words[-1])

# reversed sentence
print("Reversed:", sentence[::-1])