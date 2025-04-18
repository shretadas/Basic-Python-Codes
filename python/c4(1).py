#Write a program to store seven fruits in a list entered by the user.
def store_fruits():
    fruits = []
    for i in range(7):
        fruits.append(input(f"Enter fruit {i + 1}: "))
        print("Fruits entered:", fruits)
store_fruits()
