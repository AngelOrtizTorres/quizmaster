from typeguard import typechecked
import json
import random
import app.config as config

@typechecked
class QuestionManager:

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
            file_path = config.QUESTIONS_FILE[self.__difficulty.lower()]
            with open(file_path, 'r', encoding='utf-8') as file:
                questions = json.load(file)
                return questions.get(self.__category, [])
        except FileNotFoundError:
            print(f"Error: {file_path} file not found.")
            return []

    def get_random_questions(self, num_questions: int = 10) -> list:
        if not self.__questions:
            return []
        return random.sample(self.__questions, min(num_questions, len(self.__questions)))