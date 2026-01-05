# agent.py

from google.adk.agents import Agent
from tools import validate_move, resolve_round, update_game_state


referee_agent = Agent(
    name="RockPaperScissorsPlusReferee",
    model="gemini-1.5-flash",
    instructions="""
You are an AI referee for Rock–Paper–Scissors–Plus.

Rules:
- Best of 3 rounds
- Moves: rock, paper, scissors, bomb
- Bomb can be used once per player
- Bomb beats all except bomb vs bomb (draw)
- Invalid input wastes the round

You must use tools to validate moves, resolve rounds,
and update game state.
""",
    tools=[validate_move, resolve_round, update_game_state]
)
