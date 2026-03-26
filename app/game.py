from app.models.player import Player
import app.config as config
from app.models.question import QuestionManager
from app.storage import save_result

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
                self.__evaluate_answer(answer, question['answer'])
                
            except ValueError:
                print("Entrada no válida. Se considera como respuesta incorrecta.")
                self.__player.lose_life()
                penalty = config.POINTS_PENALTY[self.__player.difficulty]
                self.__player.sub_points(penalty)
        
        if self.__player.is_alive():
            print(f"\nFelicidades, has ganado. Tu puntuación final es: {self.__player.score}")
            save = input("¿Deseas guardar tu resultado en el ranking? (s/n): ").strip().lower()
            if save == 's':
                save_result(self.__player)
                print("Resultado guardado en el ranking.")
            else:
                print("Resultado no guardado.")
        else:
            print(f"\nHas perdido todas tus vidas. Tu puntuación final es: {self.__player.score}")
            
        input("Presiona Enter para volver al menú principal...")
            
        

    def __evaluate_answer(self, answer: int, correct_answer: int) -> bool:
        if answer == correct_answer:
            print("¡Respuesta correcta!")
            self.__player.add_points(config.POINTS_CORRECT)
        else:
            print("Respuesta incorrecta.")
            self.__player.lose_life()
            penalty = config.POINTS_PENALTY[self.__player.difficulty]
            self.__player.sub_points(penalty)


    def reset_game(self):
        self.__player.reset_lives()
        self.__player.reset_score()
        self.__questions = []

    