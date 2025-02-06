import random

playerturn = 10
class SecretWord:
    def __init__(self, word = None):
        if word is not None:
            self.word = word.upper()
            return
        with open("words.txt")as file:
            lines = file.readlines()
            word = random.choice(lines)
            self.word = word.strip().upper()

    def show_letters(self, letters):
        uppercase = [let.upper() for let in letters]
        filtered = [letter if letters in uppercase else "_" for letter in self.word]
        return " ".join(filtered)
    
    def check_letters(self, letters):
        return "_" not in self.show_letters(letters)
    
    def check(self, text):
        return self.word == text.strip().upper()

def main(turns):

    # letters tried by the player
    letters = []

    word = SecretWord()
    print(word.word)

    print(word.show_letters(letters))

    for t in range (turns):
        # ask player for a letter
        letter = ""
        while letter.upper() not in letters:
            letter = input("Need to enter a Letter !")
            if letter.upper() not in letters:
                letters.append(letter.upper())
            else:
                print("You have tried this letter already !")
        print(word.show_letters(letters))

        if word.check_letters(letters):
            print("You win!")
            return True

    print("You lost!")


if __name__ == "__main__":
    main(playerturn)
