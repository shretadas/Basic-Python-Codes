#Write a program to find whether a given username contains less than 10 characters or not.
def username():
    username=input("enter your username:")
    if len(username)<10:
        print("this username conatsins less than 10 characters")
    else:
        print("this username contains more than 10 characters")
username()