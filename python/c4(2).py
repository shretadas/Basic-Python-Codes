#Write a program to accept marks of 6 students and display them in a sorted manner.
def accept_marks():
    marks=[]
    for i in range(6):
        mark=int(input(f"enter the marks of student {i+1}: "))
        marks.append(mark)
        marks.sort()
        print("marks are:",marks)
accept_marks()