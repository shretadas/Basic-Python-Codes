#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
def empty_dict():
    favourite_language={}
    for i in range(4):
        name=input(f"enter the name of friend {i+1} : ").strip()
        language=input(f"enter {name}'s favourite language:").strip()
        favourite_language[name]=language
        print("\nFavorite languages of friends:")
        for name, language in favourite_language.items():
            print(f"{name}: {language}")
empty_dict()