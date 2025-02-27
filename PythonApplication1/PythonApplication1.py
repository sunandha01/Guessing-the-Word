
import random
import string

def get_hangman_stage(attempts):
    stages = [
        """\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n""",
        """\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n""",
        """\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n""",
        """\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n""",
        """\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n""",
        """\n  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n""",
        """\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n"""
    ]
    return stages[len(stages) - attempts - 1]

def hangman():
    word_list = ["rizz", "ohio", "sigma", "tiktok", "skibidi"]
    word = random.choice(word_list)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()
    
    print("\nWelcome to Hangman!")
    while attempts > 0:
        print(get_hangman_stage(attempts))
        print("Current word: ", ' '.join(guessed_word))
        print("Guessed letters: ", ', '.join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Great guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        if '_' not in guessed_word:
            print("\nCongratulations!! You guessed the word: ", word.upper())
            break
    else:
        print(get_hangman_stage(attempts))
        print("\nYou've run out of attempts! The word was: ", word.upper())
        
if __name__ == "__main__":
    hangman()
