hindi_to_english = {
    "नमस्ते": "Hello",
    "पानी": "Water",
    "खाना": "Food",
    "गाड़ी": "Car",
    "पुस्तक": "Book",
    "सूरज": "Sun"
}

def lookup_translation():
    while True:
        hindi_word = input("Enter a Hindi word to look up its English translation (enter 'exit' to quit): ").strip()
        
        if hindi_word.lower() == "exit":
            print("Exiting program...")
            break
        
        translation = hindi_to_english.get(hindi_word, "Translation not found")
        print(f"The English translation of '{hindi_word}' is '{translation}'")


lookup_translation()
