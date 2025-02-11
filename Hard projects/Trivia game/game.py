import json
import random
from question_library import QuestionLibrary

class Game:
    def __init__(self, filename="trivia.json", category=None, difficulty=None, number=None):
        self.questions = QuestionLibrary(filename).get_questions(category, difficulty, number)
        self.score = 0

    def play(self):
        print("\nWelcome to the Trivia Game!\n")

        for question in self.questions:
            print(question)

            while True:
                try:
                    user_input = int(input("Your answer (1-4): "))
                    if user_input in {1, 2, 3, 4}:
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if user_input == question.answer_id:
                points = {"easy": 1, "medium": 2, "hard": 3}.get(question.difficulty, 0)
                self.score += points
                print(f"Correct! You earned {points} points.\n")
            else:
                print(f"Incorrect! The correct answer was {question.answer_id}. {question.answers[question.answer_id - 1]}\n")
        
        print(f"\nGame Over! Your final score is: {self.score}/{len(self.questions) * 3} points.")
