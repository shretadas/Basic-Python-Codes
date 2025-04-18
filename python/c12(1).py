#Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
filenames = [r'C:\Users\dassh\Downloads\poems.txt', r'C:\Users\dassh\Downloads\hi-score.txt', '3.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            print(f"{filename} opened successfully")
    except FileNotFoundError:
        print(f"{filename} not found")
