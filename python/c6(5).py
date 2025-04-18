#Write a program which finds out whether a given name is present in a list or not.
def name():
    names=["david","arpan","ahana","shirshak"]
    name_find=input("enter a name to find in the list:")
    if name_find in names:
        print(f"{name_find} is present in the list")
    else:
        print(f"{name_find} is not present in the list")
name()