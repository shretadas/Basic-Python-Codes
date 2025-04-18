#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
def student():
    marks=[]
    for i in range(1,4):
        sub1=int(input("enter the marks obtained in sub1:"))
        sub2=int(input("enter the marks obtained in sub2:"))
        sub3=int(input("enter the marks obtained in sub3:"))
        
        total_marks=sub1+sub2+sub3
        percentage=(total_marks/300)*100
        if percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33:
            print("congratulations,you have passed!")
        else:
            print("you have failed")
student()

