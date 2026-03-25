import time
import app.config as config
from app.game import Game
import app.utils as utils
import app.menus as menus
from app.models.player import Player
from app.models.question import QuestionManager

utils.clear_terminal()

name = input("\nPara empezar escribe tu nombre: ")
selected_difficulty = "easy"
selected_category = "Programación"
    
def set_difficulty() -> str:
    option = menus.DIFFICULTY_MENU.choose()
    return config.DIFFICULTY_LEVELS.get(option, "easy")

def set_category() -> str:
    option = menus.CATEGORY_MENU.choose()
    return config.CATEGORIES.get(option, "Programación")

while True:
    main_option = menus.MAIN_MENU.choose()
    utils.clear_terminal()
    match main_option:
        case 1:
            name = input("\nEscribe aquí tu nombre: ")

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
            input("Pulsa ENTER para volver al menú principal...")
            utils.clear_terminal()

        case 5:
            input("\nPulsa ENTER para volver al menú principal...")
            utils.clear_terminal()

        case 6:
            player = Player(name, selected_difficulty, selected_category)
            question_manager = QuestionManager(player.difficulty, player.category)
            game = Game(player, question_manager)
            game.play()
            utils.clear_terminal()
            if player.lives > 0:
                input("Pulsa ENTER para volver al menú principal...")
                utils.clear_terminal()

        case 7:
            print(f"\n¡Nos vemos en la próxima {name}!\n")
            break

        case _:
            print("Opción no válida")