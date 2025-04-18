#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
def game():
    import random
    return random.randint(0, 100)

def update_high_score():
    filename = r'C:\Users\dassh\Downloads\hi-score.txt'
    
    try:
        with open(filename, 'r') as file:
            high_score = int(file.read().strip() or 0)
    except (FileNotFoundError, ValueError):
        high_score = 0
    
    new_score = game()
    
    if new_score > high_score:
        with open(filename, 'w') as file:
            file.write(str(new_score))
        print(f"New high score: {new_score}")
    else:
        print(f"No new high score. Current high score remains: {high_score}")


update_high_score()
