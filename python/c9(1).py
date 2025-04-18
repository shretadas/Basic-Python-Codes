#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
import os

def check_for_twinkle(filename):
    with open(filename, 'r') as file:
            content = file.read()
            if 'twinkle' in content.lower():
                return "The word 'twinkle' is present in the file."
            else:
                return "The word 'twinkle' is not found in the file."

filename = 'C:\\Users\\dassh\\Downloads\\poems.txt'
result = check_for_twinkle(filename)
print(result)
