#Write a python function which converts inches to cms.
def inches_to_cm(inches):
    cm=inches*2.54
    return cm
inches=float(input("enter the length in inches:"))
centimeters=inches_to_cm(inches)
print(f"{inches}inches is equal to {centimeters}centimeters")