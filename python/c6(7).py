#Write a program to find out whether a given post is talking about “Harry” or not.
def given_post():
    post=input("enter the post text:")
    if "Harry" in post:
        print("this post is talking about Harry")
    else:
        print("this post is not talking about Harry")

given_post()