# Exercise 6: Substring Search
sentence = input("Please enter a sentence: ")
word_to_search = input("Please enter a word to search for: ")
if word_to_search in sentence:
    position = sentence.index(word_to_search)
    print(f"The word '{word_to_search}' exists in the sentence at index {position}.")
else:
    print(f"The word '{word_to_search}' does not exist in the sentence.")
