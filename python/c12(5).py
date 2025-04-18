#Store the multiplication tables generated in problem 3 in a file named Tables.txt.
number = int(input("Enter a number: "))
multiplication_table = [number * i for i in range(1, 11)]

with open(r'C:\Users\dassh\Downloads\hi-score.txt', 'w') as file:
    for i in range(1, 11):
        file.write(f"{number} x {i} = {multiplication_table[i-1]}\n")

print(f"Multiplication table of {number} has been written to hi-score.txt")
