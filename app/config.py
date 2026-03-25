DIFFICULTY_LEVELS = {1: 'fácil', 2: 'medio', 3: 'difícil'}
CATEGORIES = {1: 'General', 2: 'Ciencia', 3: 'Historia', 4: 'Deportes', 5: 'Entretenimiento', 6: 'Programación'}

QUESTIONS_FILE = {'fácil': 'data/questions/easy.json', 'medio': 'data/questions/medium.json', 'difícil': 'data/questions/hard.json'}
RANKING_FILE = 'data/ranking.json'

QUESTIONS_PER_GAME = 10
POINTS_CORRECT = 5
POINTS_PENALTY = {1: 1, 2: 2, 3: 3}  # Penalty points based on difficulty level