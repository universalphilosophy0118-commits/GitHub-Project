sentence = input("Enter a sentence:")

vowels = "aeiouAEIOU"

vowel_count = 0

for letter in sentence:
    if letter in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)