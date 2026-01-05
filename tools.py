# tools.py

from typing import Dict
from google.adk.tools import tool
from state import game_state, VALID_MOVES


@tool
def validate_move(move: str, is_user: bool) -> Dict:
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb":
        if is_user and game_state["user_bomb_used"]:
            return {"valid": False, "reason": "User already used bomb"}
        if not is_user and game_state["bot_bomb_used"]:
            return {"valid": False, "reason": "Bot already used bomb"}

    return {"valid": True, "move": move}


@tool
def resolve_round(user_move: str, bot_move: str) -> Dict:
    if user_move == bot_move:
        return {"winner": "draw"}

    if user_move == "bomb" and bot_move != "bomb":
        return {"winner": "user"}

    if bot_move == "bomb" and user_move != "bomb":
        return {"winner": "bot"}

    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if rules[user_move] == bot_move:
        return {"winner": "user"}

    return {"winner": "bot"}


@tool
def update_game_state(winner: str, user_move: str, bot_move: str) -> Dict:
    game_state["round"] += 1

    if user_move == "bomb":
        game_state["user_bomb_used"] = True
    if bot_move == "bomb":
        game_state["bot_bomb_used"] = True

    if winner == "user":
        game_state["user_score"] += 1
    elif winner == "bot":
        game_state["bot_score"] += 1

    return game_state
