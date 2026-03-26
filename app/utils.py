import os

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