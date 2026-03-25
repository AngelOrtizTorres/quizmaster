import time
import app.config as config
from app.game import Game
import app.menus as menus
from app.models.player import Player
from app.models.question import QuestionManager

config.clear_terminal()

name = input("\nPara empezar escribe tu nombre: ")
selected_difficulty = "easy"
selected_category = "Programación"

while True:
    main_option = menus.MAIN_MENU.choose()
    config.clear_terminal()
    match main_option:
        case 1:
            name = input("\nEscribe aquí tu nombre: ")

        case 2:
            selected_difficulty = Game.set_difficulty()
            print(f"\nHas elegido dificultad: {selected_difficulty}")
            time.sleep(1.5)
            config.clear_terminal()

        case 3:
            selected_category = Game.set_category()
            print(f"\nHas elegido categoría: {selected_category}")
            time.sleep(1.5)
            config.clear_terminal()            

        case 4:
            input("Pulsa ENTER para volver al menú principal...")
            config.clear_terminal()

        case 5:
            input("\nPulsa ENTER para volver al menú principal...")
            config.clear_terminal()

        case 6:
            player = Player(name, selected_difficulty, selected_category)
            question_manager = QuestionManager(player.difficulty, player.category)
            game = Game(player, question_manager)
            game.play()
            config.clear_terminal()
            if player.lives > 0:
                input("Pulsa ENTER para volver al menú principal...")
                config.clear_terminal()

        case 7:
            print(f"\n¡Nos vemos en la próxima {name}!\n")
            break

        case _:
            print("Opción no válida")