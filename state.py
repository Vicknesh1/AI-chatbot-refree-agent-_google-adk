# state.py

game_state = {
    "round": 0,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False
}

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]
MAX_ROUNDS = 3
