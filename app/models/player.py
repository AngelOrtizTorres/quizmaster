from typeguard import typechecked
from app.models.lifelines import FiftyFifty, Hint, Roulette
    
@typechecked
class Player:
    
    def __init__(self, name: str, difficulty: str, category: str):
        self.__name = name
        self.__difficulty = difficulty
        self.__category = category
        self.__lives = 3
        self.__score = 0
        self.__fifty_fifty = FiftyFifty()
        self.__hint = Hint()
        self.__roulette = Roulette()

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def difficulty(self) -> str:
        return self.__difficulty
    
    @property
    def category(self) -> str:
        return self.__category
    
    @property
    def lives(self) -> int:
        return self.__lives
    
    @property
    def score(self) -> int:
        return self.__score
    
    @property
    def fifty_fifty(self) -> FiftyFifty:
        return self.__fifty_fifty
    
    @property
    def hint(self) -> Hint:
        return self.__hint
    
    @property
    def roulette(self) -> Roulette:
        return self.__roulette
    
    def reset_lives(self):
        self.__lives = 3

    def lose_life(self):
        if self.__lives > 0:
            self.__lives -= 1

    def is_alive(self) -> bool:
        return self.__lives > 0

    def add_points(self, score: int):
        self.__score += score

    def sub_points(self, score: int):
        self.__score = max(0, self.__score - score)

    def reset_score(self):
        self.__score = 0
    