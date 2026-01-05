# main.py

import random
from state import game_state, MAX_ROUNDS
from tools import validate_move, resolve_round, update_game_state


def bot_choose_move():
    if not game_state["bot_bomb_used"] and random.random() < 0.15:
        return "bomb"
    return random.choice(["rock", "paper", "scissors"])


def main():
    print("\n🎮 Rock–Paper–Scissors–Plus 🎮")
    print("Best of 3 rounds. Type your move.\n")

    while game_state["round"] < MAX_ROUNDS:
        print(f"--- Round {game_state['round'] + 1} ---")
        user_input = input("Your move: ")

        user_validation = validate_move(user_input, True)

        if not user_validation["valid"]:
            print(f"❌ Invalid move: {user_validation['reason']}")
            game_state["round"] += 1
            continue

        user_move = user_validation["move"]
        bot_move = bot_choose_move()

        bot_validation = validate_move(bot_move, False)
        bot_move = bot_validation["move"]

        result = resolve_round(user_move, bot_move)
        update_game_state(result["winner"], user_move, bot_move)

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")

        if result["winner"] == "draw":
            print("⚖️ Round result: Draw")
        elif result["winner"] == "user":
            print("✅ You win this round")
        else:
            print("❌ Bot wins this round")

        print(
            f"Score → You: {game_state['user_score']} | "
            f"Bot: {game_state['bot_score']}\n"
        )

    print("🏁 Game Over!")
    if game_state["user_score"] > game_state["bot_score"]:
        print("🎉 Final Result: YOU WIN")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("🤖 Final Result: BOT WINS")
    else:
        print("🤝 Final Result: DRAW")


if __name__ == "__main__":
    main()
