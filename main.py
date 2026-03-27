import time
import app.config as config
from app.game import Game
from app.storage import get_top3
import app.utils as utils
import app.menus as menus
from app.models.player import Player
from app.models.question import QuestionManager

utils.clear_terminal()

while True:
    name = input("\nPara empezar escribe tu nombre: ").strip()
    if name:
        utils.clear_terminal()
        break
    print("El nombre no puede estar vacío. Inténtalo de nuevo.")
    
selected_difficulty = ""
selected_category = ""
    
def set_difficulty() -> str:
    option = menus.DIFFICULTY_MENU.choose()
    return config.DIFFICULTY_LEVELS.get(option)

def set_category() -> str:
    option = menus.CATEGORY_MENU.choose()
    return config.CATEGORIES.get(option)

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
            print("Top 3 jugadores por dificultad:")

            print("\nFácil:")
            top = get_top3("easy")
            if top:
                for i, r in enumerate(top, start=1):
                    print(f"{i}. {r['name']} - {r['category']} - {r['score']} pts - {r['lives']} vidas")
            else:
                print("  (sin resultados)")

            print("\nMedia:")
            top = get_top3("medium")
            if top:
                for i, r in enumerate(top, start=1):
                    print(f"{i}. {r['name']} - {r['category']} - {r['score']} pts - {r['lives']} vidas")
            else:
                print("  (sin resultados)")

            print("\nDifícil:")
            top = get_top3("hard")
            if top:
                for i, r in enumerate(top, start=1):
                    print(f"{i}. {r['name']} - {r['category']} - {r['score']} pts - {r['lives']} vidas")
            else:
                print("  (sin resultados)")

            input("\nPulsa ENTER para volver al menú principal...")
            utils.clear_terminal()

        case 6:
            if not selected_difficulty or not selected_category:
                print("\nDebes elegir categoría y dificultad antes de jugar.")
                input("Pulsa ENTER para volver al menú principal...")
                utils.clear_terminal()
                continue

            player = Player(name, selected_difficulty, selected_category)
            question_manager = QuestionManager(player.difficulty, player.category)
            game = Game(player, question_manager)
            game.play()

            # Al terminar la partida, forzar a re-elegir categoría y dificultad
            selected_difficulty = ""
            selected_category = ""
            utils.clear_terminal()

        case 7:
            print(f"\n¡Nos vemos en la próxima {name}!\n")
            break

        case _:
            print("Opción no válida")