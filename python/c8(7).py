#Write a python function to remove a given word from a list ad strip it at the same time.
def remove_and_strip(word_to_remove, word_list):
    return [word.strip() for word in word_list if word.strip() != word_to_remove.strip()]


words = input("Enter words separated by spaces: ").split()
word_to_remove = input("Enter the word to remove: ")
filtered_words = remove_and_strip(word_to_remove, words)

print("Filtered words:", filtered_words)

