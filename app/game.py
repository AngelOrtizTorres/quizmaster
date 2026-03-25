from app.models.player import Player
import app.config as config
from app.models.question import QuestionManager
import app.menus as menu

class Game:

    def __init__(self, player: Player, question_manager: QuestionManager):
        self.__player = player
        self.__questions = question_manager.get_random_questions(config.QUESTIONS_PER_GAME)

    @property
    def player(self) -> Player:
        return self.__player
    
    @property
    def questions(self) -> QuestionManager:
        return self.__questions
    
    def play(self):
        for question in self.__questions:
            if not self.__player.is_alive():
                print("¡Has perdido todas tus vidas! Fin del juego.")
                break
            
            print(f"\nPregunta: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            
            try:
                answer = int(input("Introduce el número de tu respuesta: "))
                if answer == question['answer']:
                    print("¡Respuesta correcta!")
                    self.__player.add_points(config.POINTS_CORRECT)
                else:
                    print("Respuesta incorrecta.")
                    self.__player.lose_life()
                    penalty = config.POINTS_PENALTY[self.__player.difficulty]
                    self.__player.sub_points(penalty)
            except ValueError:
                print("Entrada no válida. Se considera como respuesta incorrecta.")
                self.__player.lose_life()
                penalty = config.POINTS_PENALTY[self.__player.difficulty]
                self.__player.sub_points(penalty)
        
        print(f"\nJuego terminado. Tu puntuación final es: {self.__player.score}")
        input("Presiona Enter para volver al menú principal...")


    def reset_game(self):
        self.__player.reset_lives()
        self.__player.add_points(-self.__player.score)  # Reset score to 0
        self.__questions = []

    @staticmethod
    def set_difficulty() -> str:
        option = menu.DIFFICULTY_MENU.choose()
        # Devuelve el valor en inglés
        return config.DIFFICULTY_LEVELS.get(option, "easy")

    @staticmethod
    def set_category() -> str:
        option = menu.CATEGORY_MENU.choose()
        return config.get_category_name(option)