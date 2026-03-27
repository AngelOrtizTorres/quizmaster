from colorama import Fore, Style
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
                break
            
            print(f"\nPregunta: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            
            try:
                options = question['options']
                correct = question['options'][question['answer'] - 1]

                while True:
                    use = input("\n¿Deseas usar un comodín? (s/n): ").strip().lower()
                    if use != 's':
                        break

                    available = []
                    if self.__player.fifty_fifty.is_available:
                        available.append('f: 50/50')
                    if self.__player.hint.is_available:
                        available.append('h: pista')
                    if self.__player.roulette.is_available:
                        available.append('r: ruleta')

                    if not available:
                        print("No te quedan comodines.")
                        break

                    print("Comodines disponibles: " + " | ".join(available))
                    choice = input("Elige un comodín: ").strip().lower()

                    if choice == 'f' and self.__player.fifty_fifty.is_available:
                        options = self.__player.fifty_fifty.use(options, correct)
                        print("\nOpciones tras 50/50:")
                        for idx, opt in enumerate(options, 1):
                            print(f"{idx}. {opt}")

                    elif choice == 'h' and self.__player.hint.is_available:
                        print(f"\nPista: {self.__player.hint.use(question['hint'])}")

                    elif choice == 'r' and self.__player.roulette.is_available:
                        options = self.__player.roulette.use(options, correct)
                        print("\nOpciones tras ruleta:")
                        for idx, opt in enumerate(options, 1):
                            print(f"{idx}. {opt}")

                    else:
                        print("Opción no válida o comodín ya usado.")


                answer = int(input("Introduce el número de tu respuesta: "))
                self.__evaluate_answer(answer, options, correct)
                
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
            
        

    def __evaluate_answer(self, answer: int, options: list, correct_option: str) -> None:
        if 1 <= answer <= len(options):
            selected = options[answer - 1]
            if selected == correct_option:
                print(Fore.GREEN + "¡Respuesta correcta!" + Style.RESET_ALL)
                self.__player.add_points(config.POINTS_CORRECT)
            else:
                print(Fore.RED + "Respuesta incorrecta." + Style.RESET_ALL)
                self.__player.lose_life()
                self.__player.sub_points(config.POINTS_PENALTY[self.__player.difficulty])
        else:
            print("Opción no válida.")
            self.__player.lose_life()
            self.__player.sub_points(config.POINTS_PENALTY[self.__player.difficulty])

    