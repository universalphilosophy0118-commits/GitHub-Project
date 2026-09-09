text = input("Enter a word or sentence: ")

text = text.lower()

characters = {}

for letter in text:
    if letter == " ":
        continue

    if letter in characters:
        characters[letter] += 1
    else:
        characters[letter] = 1
print("Character count:")

for letter, count in characters.items():
    print(letter, ":", count)