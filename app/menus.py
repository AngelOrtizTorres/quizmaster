from app.menu import Menu

MAIN_MENU = Menu("Cambiar nombre del jugador","Elegir dificultad del juego", "Elegir categoría de las preguntas", "Leer instrucciones",
                 "Ver la clasificación", "Empezar a jugar", "Salir", title = "QuizMaster - Menú Principal")

DIFFICULTY_MENU = Menu("Dificultad Fácil", "Dificultad Media", "Dificultad Difícil",
                       title = "\nELIGE UNA DIFICULTAD")

CATEGORY_MENU = Menu(
    "General", "Ciencia", "Historia", "Deportes", "Videojuegos", "Programación",
    title="\nELIGE LA CATEGORÍA DE LAS PREGUNTAS"
)