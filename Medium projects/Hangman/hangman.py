import random
import sys

def reveal_letters(word, letters):
    # Reveals guessed letters in the word.
    return " ".join([char.upper() if char.upper() in letters else "_" for char in word])

def all_letters_found(word, letters):
    # Checks if all letters in the word have been guessed.
    return all(char.upper() in letters for char in word)

def pick_random_word():
    # Picks a random word from words.txt.
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)

def hangman(turns=10, word=None):
    #Main Hangman game logic.

    # Starts the game 
    print("\nWelcome to the hangman game !")

    # if the word not chosen goes to the pick_random_word function 
    if not word:
        word = pick_random_word()
    letters_tried = [] # the tried letters are sent to this
    turns_left = turns # the turns left are gone back to the turns

    while turns_left > 0: # turns greates tha 0 then the game is running 
        print("\nWord:", reveal_letters(word, letters_tried)) # prints the reveal letter function 
        print("Turns left:", turns_left)
        guess = input("Guess a letter: ").upper() # asks the user for input of the letter 

        if len(guess) == 1 and guess.isalpha():
            if guess in letters_tried:
                print("You already tried that letter.")
                continue    # checks the len of the guess and if the letter has been tried or nah 
            letters_tried.append(guess)
        elif guess == word.upper():
            print("\nYOU WON! You guessed the word:", word)
            return
        else:
            print("Invalid input. Please enter a single letter:")
            continue

        if all_letters_found(word, letters_tried):
            print("\nYOU WON! The word was:", word)
            return

        turns_left -= 1

    print("\nGAME OVER! The word was:", word)

if __name__ == "__main__":
    turns = 10
    word = None

    if len(sys.argv) > 1:
        turns = int(sys.argv[1])
    if len(sys.argv) > 2:
        word = sys.argv[2]

    hangman(turns, word)