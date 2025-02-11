from question import Question
import json
import random

class QuestionLibrary:
    def __init__(self, filename= "trivia.json"):
       with open(filename, "r") as file:
            data = json.load(file)
            self.questions = [Question(**question) for question in data]

    def __len__(self):
        return len(self.questions)
    
    def get_categories(self):
        return list(set(question.category for question in self.questions))
    
    def get_questions(self, category=None, difficulty=None, number=None):
        filtered_questions = self.questions

        if category:
            filtered_questions = [question for question in filtered_questions if question.category == category]
        
        if difficulty in {"easy", "medium", "hard"}:
            filtered_questions = [question for question in filtered_questions if question.difficulty == difficulty]
        
        random.shuffle(filtered_questions)
        if number is not None:
            return filtered_questions[:min(number, len(filtered_questions))]

        return filtered_questions