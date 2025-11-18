# Developer Guide

## Problem & Overall Approach
- **Goal**: deliver a fully playable Battleship experience in the terminal, supporting human-vs-human and human-vs-computer matches.
- **Approach**: keep the core loop simple (`Game` orchestrates setup/play), encapsulate gameplay rules in `Player`, `Ship`, and `Board`, and isolate utilities (coordinates, colors, RNG, AI) in `src/utils`.

## Environment & Tooling
- **Python**: 3.10+ (uses only standard library).
- **Recommended shell**: Windows PowerShell or Windows Terminal (ANSI colors enabled).
- **Dependencies**: none beyond Python. Optional formatters/linters (e.g., `black`, `ruff`) can be installed manually.

### Quick setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
# (No runtime dependencies yet)
```

## Project Layout
```
src/
  main.py          # CLI entry point
  game.py          # Game orchestration and loops
  player.py        # Player model and turn drivers (human/computer)
  board.py         # 10x10 board with render helpers
  ship.py          # Ship model and placement validation
  utils/
    aimbot.py      # Computer aiming strategy
    cmd_utils.py   # Terminal helpers
    colors.py      # ANSI color helpers
    coordinate.py  # Coordinate value object & parsing helpers
    random_gen.py  # Random placement utilities
    shot_result.py # Enum describing shot outcomes
```

## Execution Flow
1. `main.py` clears the terminal, prompts for game type (`a` vs human, `b` vs computer), then instantiates `Game`.
2. `Game.setup()` collects player names, handles manual ship placement (with validation) or uses `random_gen.generate_random_ships_for_player` for the AI.
3. `Game.play()` dispatches to `two_player_game` or `agains_computer` which:
   - rotates turns,
   - calls `Player.shoot_at()` (human input or `AimBot.fire_shot`),
   - updates `Board` objects through `Player.validate_shot_against`.
4. End-game detection checks `Player.ships` for `Ship.is_sunk`. `Game.print_game_results` renders both boards side-by-side.

## Core Components
- **Board (`board.Board`)**: stores `Coordinate` lists for misses, hits, ships and handles ASCII rendering with `utils.colors.ANSI`.
- **Ship (`ship.Ship`)**: wraps contiguous coordinates, exposes `try_hit`, `check_if_is_touching`, and `check_if_coordinates_are_valid_for_ship` for validation.
- **Player (`player.Player`)**: tracks ships, tried coordinates, game & ship boards; mediates human input (`human_turn`) or AI turns (`computer_turn`).
- **AimBot (`utils.aimbot.AimBot`)**: stores last hits, deduces direction, and searches until a ship is sunk; falls back to random coordinates via `utils.random_gen`.
- **ShotResult (`utils.shot_result.Shot_Result`)**: enum for `MISSED`, `HIT`, `SINKED`, `TRIED`. Used throughout to control turn flow.

## Coordinate & Input Rules
- Coordinates are strings with digit + uppercase letter (e.g., `3A`).
- Validation lives in `utils.coordinate.check_coordinates` and is reused for ship placement and firing input.
- Boards store coordinates as `Coordinate` objects; always convert before equality checks.

## Testing & Debugging
- **Existing unit tests** live alongside the main modules: see `src/test_coordinate.py` and `src/test_ship.py`. Add more `test_*.py` files in `src/` to expand coverage.
- **Run tests with pytest** once it is installed in the active virtual environment:

```powershell
pip install pytest
python -m pytest src
```