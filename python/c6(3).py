"""A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams."""
def spam_comment():
    comment=input("enter your comment:")
    if "make a lot of money"in comment.lower()or"buy now"in comment.lower()or"subscribe now"in comment.lower()or "click this"in comment.lower():
        print("this comment is a spam")
    else:
        print("this comment is not a spam")
spam_comment()
