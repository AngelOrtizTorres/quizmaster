import random
import app.config as config

class FiftyFifty:

    def __init__(self):
        self.is_available = True

    def use(self, options: list, correct_option) -> list:
        if not self.is_available:
            return options
        incorrect = [opt for opt in options if opt != correct_option]
        to_remove = random.sample(incorrect, 2)
        self.is_available = False
        return [opt for opt in options if opt not in to_remove]


class Hint:

    def __init__(self):
        self.is_available = True

    def use(self, hint_text: str) -> str:
        if not self.is_available:
            return "Ya usaste este comodín."
        self.is_available = False
        return hint_text


class Roulette:

    def __init__(self):
        self.is_available = True

    def use(self, options: list, correct_option) -> list:
        if not self.is_available:
            return options
        incorrect = [opt for opt in options if opt != correct_option]
        num_to_remove = random.randint(0, config.ROULETTE_MAX_REMOVE)
        to_remove = random.sample(incorrect, min(num_to_remove, len(incorrect)))
        self.is_available = False
        return [opt for opt in options if opt not in to_remove]