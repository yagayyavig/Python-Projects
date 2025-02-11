import random
import re

class Question:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.category = category
        self.difficulty = difficulty

        if difficulty not in {"easy", "medium", "hard"}:
            raise AttributeError("Invalid difficulty. Must be 'easy', 'medium', or 'hard'.")
        

        self.answers = self.incorrect_answers + [self.correct_answer]
        random.shuffle(self.answers)

        self.answer_id = self.answers.index(self.correct_answer) + 1
    
    def __str__(self):
        output = f"{self.question}\n"

        for index, answer in enumerate(self.answers, start=1):
            output += f"{index}. {answer}\n"

        return output.strip()