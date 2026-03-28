import time
import app.config as config
from app.game import Game
from app.storage import show_ranking
import app.utils as utils
import app.menus as menus
from app.models.player import Player
from app.models.question import QuestionManager

def set_difficulty() -> str:
    option = menus.DIFFICULTY_MENU.choose()
    return config.DIFFICULTY_LEVELS.get(option)

def set_category() -> str:
    option = menus.CATEGORY_MENU.choose()
    return config.CATEGORIES.get(option)

def main():

    utils.clear_terminal()

    while True:
        name = input("\nPara empezar escribe tu nombre: ").strip()
        if name:
            utils.clear_terminal()
            break
        print("El nombre no puede estar vacío. Inténtalo de nuevo.")

    selected_difficulty = ""
    selected_category = ""

    while True:
        main_option = menus.MAIN_MENU.choose()
        utils.clear_terminal()
        match main_option:
            case 1:
                while True:
                    new_name = input("\nEscribe aquí tu nombre: ").strip()
                    if new_name:
                        name = new_name
                        utils.clear_terminal()
                        break
                    print("El nombre no puede estar vacío. Inténtalo de nuevo.")

            case 2:
                selected_difficulty = set_difficulty()
                print(f"\nHas elegido dificultad: {config.DIFFICULTY_DISPLAY[selected_difficulty]}")
                time.sleep(1.5)
                utils.clear_terminal()

            case 3:
                selected_category = set_category()
                print(f"\nHas elegido categoría: {selected_category}")
                time.sleep(1.5)
                utils.clear_terminal()            

            case 4:
                utils.show_instructions()
                input("Pulsa ENTER para volver al menú principal...")
                utils.clear_terminal()

            case 5:
                show_ranking()
                input("\nPulsa ENTER para volver al menú principal...")
                utils.clear_terminal()

            case 6:
                if not selected_difficulty or not selected_category:
                    print("\nDebes elegir categoría y dificultad antes de jugar.")
                    input("Pulsa ENTER para volver al menú principal...")
                    utils.clear_terminal()
                    continue
                
                player = Player(name, selected_difficulty, selected_category)
                try:
                    question_manager = QuestionManager(player.difficulty, player.category)
                    game = Game(player, question_manager)
                    game.play()
                except FileNotFoundError as e:
                    print(f"\nError: {e}")
                    input("Pulsa ENTER para volver al menú principal...")
                utils.clear_terminal()

            case 7:
                print(f"\n¡Nos vemos en la próxima {name}!\n")
                break

            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()