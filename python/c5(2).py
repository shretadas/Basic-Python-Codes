#Write a program to input eight numbers from the user and display all the unique numbers (once).
def number_counts():
    number_counts={}

    for i in range(8):
        num=int(input(f"enter the numbers {i+1}: "))
    number_counts[num]=number_counts.get(num,0)+1
    print("unique numbers entered:")
    for num,count in number_counts.items():
        print(f"{num}: {count} time(s)")
number_counts()