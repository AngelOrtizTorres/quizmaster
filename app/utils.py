import os
import time
from colorama import Fore, Style
import app.config as config

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_instructions():
    print("""
    INSTRUCCIONES
    =============
    
    - Responde 10 preguntas de opción múltiple.
    - Tienes 3 vidas. Cada fallo resta una vida.
    - Si pierdes todas las vidas, la partida termina.
    - Puntos por acierto: 5 pts.
    - Penalización por fallo según dificultad:
        Fácil: -1 pt / Media: -2 pts / Difícil: -3 pts
    - Al terminar puedes guardar tu resultado en el ranking.
    """)

def get_banner():
    ascii_banner = r"""
   ____        _     __  __           _            
  / __ \      (_)   |  \/  |         | |           
 | |  | |_   _ _ ___| \  / | __ _ ___| |_ ___ _ __ 
 | |  | | | | | |_  / |\/| |/ _` / __| __/ _ \ '__|
 | |__| | |_| | |/ /| |  | | (_| \__ \ ||  __/ |   
  \___\_\\__,_|_/___|_|  |_|\__,_|___/\__\___|_|   
                                                   
"""
    return Fore.CYAN + ascii_banner + Style.RESET_ALL

def counter_start():
    banner_number3 = (Fore.YELLOW + r"""
     ____ 
    |__ /  
     |_ \
    |___/
    """)

    banner_number2 = (Fore.BLUE + r"""
     ___ 
    |_  )
     / / 
    /___|
    """)

    banner_number1 =(Fore.YELLOW + r"""
     _ 
    / |
    | |
    |_|
    """)

    banner_go = (Fore.BLUE + r"""
     ___  ___    _ 
    / __|/ _ \  | |
   | (_ | (_) | |_|
    \___|\___/  (_)  
    """ + Style.RESET_ALL)

    banners = [banner_number3, banner_number2, banner_number1, banner_go]
    
    for banner in banners:
        clear_terminal()
        print(banner)
        time.sleep(config.UI_DELAY_COUNTDOWN)
    
    clear_terminal()