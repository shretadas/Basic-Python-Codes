#Write a program to fill in a letter template given below with name and date.
def fill_letter_template():
    name=(input("enter the name:"))
    date=(input("enter the date:"))
    letter = '''Dear {name},
    You are selected!
    Date: {date}'''
    filled_letter = letter.format(name=name, date=date) 
    print(filled_letter)
fill_letter_template()