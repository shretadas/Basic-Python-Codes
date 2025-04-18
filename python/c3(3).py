#Write a program to detect double space in a string.
def detect_double_space():
    doublespace=input("enter the string:")
    if '  ' in doublespace:
        print("the double space is present in the string")
    else:
        print("the double space is not present in the string")
detect_double_space()