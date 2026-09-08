sentence = input("Enter a sentence;")

words = sentence.split()

word_count = len(words)

character_count = len(sentence.replace(" ", ""))

print("Your sentence has", character_count, "characters.")

print("Your sentences has", word_count, "Words.")
