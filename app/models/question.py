from typeguard import typechecked
import json
import random
import app.config as config

@typechecked
class Question:

    def __init__(self, difficulty: str, category: str):
        self.__difficulty = difficulty
        self.__category = category
        self.__questions = self.__load_questions()

    @property
    def difficulty(self) -> str:
        return self.__difficulty
    
    @property
    def category(self) -> str:
        return self.__category
    
    def __load_questions(self) -> list:
        try:
            with open(config.QUESTIONS_FILE, 'r') as file:
                questions = json.load(file)
                return questions.get(self.__difficulty, {}).get(self.__category, [])
        except FileNotFoundError:
            print(f"Error: {config.QUESTIONS_FILE} file not found.")
            return []

    def get_random_questions(self, num_questions: int = 10) -> list:
        if not self.__questions:
            return []
        return random.sample(self.__questions, min(num_questions, len(self.__questions)))