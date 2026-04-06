import app.utils as utils
from colorama import Fore, Style
from app.models.player import Player
import app.config as config
from app.models.question import QuestionManager
from app.storage import ask_save_results

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
        if not self.__questions:
            print("\nNo hay preguntas disponibles para esta categoría y dificultad.")
            input("Presiona Enter para volver al menú principal...")
            return
        
        utils.counter_start()
        
        for question in self.__questions:
            if not self.__player.is_alive():
                break
            
            print(f"\nPregunta: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            
            options = question['options']
            correct = question['options'][question['answer'] - 1]

            while True:
                while True:
                    use = input("\n¿Deseas usar un comodín? (s/n): ").strip().lower()
                    if use in [config.CONFIRM_YES, config.CONFIRM_NO]:
                        break
                    else:
                        print("Por favor introduce 's' o 'n'")
                
                if use != config.CONFIRM_YES:
                    break

                available = []
                if self.__player.fifty_fifty.is_available:
                    available.append(f'{config.LIFELINE_COMMAND_FIFTY}: 50/50')
                if self.__player.hint.is_available:
                    available.append(f'{config.LIFELINE_COMMAND_HINT}: pista')
                if self.__player.roulette.is_available:
                    available.append(f'{config.LIFELINE_COMMAND_ROULETTE}: ruleta')

                if not available:
                    print("No te quedan comodines.")
                    break

                print("Comodines disponibles: " + " | ".join(available))
                choice = input("Elige un comodín: ").strip().lower()

                if choice == config.LIFELINE_COMMAND_FIFTY and self.__player.fifty_fifty.is_available:
                    options = self.__player.fifty_fifty.use(options, correct)
                    print("\nOpciones tras 50/50:")
                    for idx, opt in enumerate(options, 1):
                        print(f"{idx}. {opt}")

                elif choice == config.LIFELINE_COMMAND_HINT and self.__player.hint.is_available:
                    print(f"\nPista: {self.__player.hint.use(question['hint'])}")

                elif choice == config.LIFELINE_COMMAND_ROULETTE and self.__player.roulette.is_available:
                    options = self.__player.roulette.use(options, correct)
                    print("\nOpciones tras ruleta:")
                    for idx, opt in enumerate(options, 1):
                        print(f"{idx}. {opt}")

                else:
                    print("Opción no válida o comodín ya usado.")

            while True:
                try:
                    answer = int(input("Introduce el número de tu respuesta: "))
                    if 1 <= answer <= len(options):
                        break
                    else:
                        print(f"Por favor introduce un número entre 1 y {len(options)}")
                except ValueError:
                    print("Por favor introduce un número válido")
            
            self.__evaluate_answer(answer, options, correct)

            print(f"\nExplicación: {question['explanation']}")
            input("\nPresiona Enter para continuar...")
            utils.clear_terminal()
        
        if self.__player.is_alive():
            print(f"\nFelicidades, has ganado. Tu puntuación final es: {self.__player.score}")
            ask_save_results(self.__player)
        else:
            print(f"\nHas perdido todas tus vidas. Tu puntuación final es: {self.__player.score}")
            
        input("Presiona Enter para volver al menú principal...")
            
    def __evaluate_answer(self, answer: int, options: list, correct_option: str) -> None:
        selected = options[answer - 1]
        if selected == correct_option:
            print(Fore.GREEN + "¡Respuesta correcta!" + Style.RESET_ALL)
            self.__player.add_points(config.POINTS_CORRECT)
        else:
            print(Fore.RED + "Respuesta incorrecta." + Style.RESET_ALL)
            self.__player.lose_life()
            self.__player.sub_points(config.POINTS_PENALTY[self.__player.difficulty])