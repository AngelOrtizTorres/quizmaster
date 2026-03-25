DIFFICULTY_LEVELS = {1: 'easy', 2: 'medium', 3: 'hard'}
DIFFICULTY_DISPLAY = {'easy': 'Fácil', 'medium': 'Medio', 'hard': 'Difícil'}
CATEGORIES = {1: 'General', 2: 'Ciencia', 3: 'Historia', 4: 'Deportes', 5: 'Videojuegos', 6: 'Programación'}

QUESTIONS_FILE = {'easy': 'data/questions/easy.json', 'medium': 'data/questions/medium.json', 'hard': 'data/questions/hard.json'}
RANKING_FILE = 'data/ranking.json'

QUESTIONS_PER_GAME = 10
POINTS_CORRECT = 5
POINTS_PENALTY = {'easy': 1, 'medium': 2, 'hard': 3}  # Penalty points based on difficulty level
