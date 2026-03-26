import json
import os
import app.config as config

def load_ranking() -> list:
    if not os.path.exists(config.RANKING_FILE):
        return []
    with open(config.RANKING_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_result(player) -> None:
    ranking = load_ranking()
    ranking.append({
        'name': player.name,
        'difficulty': player.difficulty,
        'category': player.category,
        'score': player.score,
        'lives': player.lives
    })
    with open(config.RANKING_FILE, 'w', encoding='utf-8') as f:
        json.dump(ranking, f, ensure_ascii=False, indent=4)

def get_top3(difficulty: str) -> list:
    ranking = load_ranking()
    filtered = [r for r in ranking if r['difficulty'] == difficulty]
    return sorted(filtered, key=lambda x: (-x['score'], -x['lives']))[:3]