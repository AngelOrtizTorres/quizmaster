# ==================== GAME DIFFICULTY & CATEGORIES ====================
DIFFICULTY_LEVELS = {1: 'easy', 2: 'medium', 3: 'hard'}
DIFFICULTY_DISPLAY = {'easy': 'Fácil', 'medium': 'Medio', 'hard': 'Difícil'}
CATEGORIES = {
    1: 'General',
    2: 'Ciencia',
    3: 'Historia',
    4: 'Deportes',
    5: 'Videojuegos',
    6: 'Programación'
}

# ==================== FILE PATHS ====================
QUESTIONS_FILE = {
    'easy': 'data/questions/easy.json',
    'medium': 'data/questions/medium.json',
    'hard': 'data/questions/hard.json'
}
RANKING_FILE = 'data/ranking.json'

# ==================== GAME MECHANICS ====================
QUESTIONS_PER_GAME = 10
INITIAL_LIVES = 3
POINTS_CORRECT = 5
POINTS_PENALTY = {
    'easy': 1,
    'medium': 2,
    'hard': 3
}
RANKING_TOP_LIMIT = 3

# ==================== LIFELINES CONFIGURATION ====================
ROULETTE_MAX_REMOVE = 3  # Maximum options removed by roulette

# ==================== UI TIMING (seconds) ====================
UI_DELAY_AFTER_SELECTION = 1.5  # Delay after difficulty/category selection
UI_DELAY_COUNTDOWN = 1  # Delay between countdown numbers

# ==================== USER COMMANDS ====================
# Lifeline Commands
LIFELINE_COMMAND_FIFTY = 'f'
LIFELINE_COMMAND_HINT = 'h'
LIFELINE_COMMAND_ROULETTE = 'r'

# Confirmation Commands
CONFIRM_YES = 's'
CONFIRM_NO = 'n'
