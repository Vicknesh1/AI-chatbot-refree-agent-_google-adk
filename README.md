 AI-chatbot-refree-agent-_google-adk
AI referee chatbot for Rock–Paper–Scissors–Plus built using Google ADK, featuring tool-based state management and rule enforcement.

 Overview
This project implements a minimal AI referee chatbot for a Rock–Paper–Scissors–Plus game.
The bot enforces rules, tracks state, and provides clear round-by-round feedback.
The game runs in a simple CLI-based conversational loop.

 State Model
The game state is maintained in-memory using a Python dictionary:
- round (int)
- user_score (int)
- bot_score (int)
- user_bomb_used (bool)
- bot_bomb_used (bool)

State does not live in the prompt and is mutated only through explicit tools.

 Agent & Tool Design
A single ADK Agent acts as the referee.
Explicit tools are used for:
- `validate_move`: checks move validity and bomb usage
- `resolve_round`: determines the winner based on game rules
- `update_game_state`: updates round count, scores, and bomb usage

This cleanly separates intent understanding, game logic, and response generation.

 Tradeoffs
 The bot’s move strategy is intentionally simple (random with low bomb probability).
 CLI interface is minimal to focus on logic correctness and state handling.

 Improvements With More Time
- Smarter bot strategy
- Replay or reset option
- Structured JSON output mode for UI integration
- Unit tests for game logic

