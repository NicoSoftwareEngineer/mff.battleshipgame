**Overview**
- **Project**: `mff.battleshipgame` — a terminal-based Battleship game implemented in Python.
- **Purpose**: Play Battleship vs another human or a computer.

**Requirements**
- **Python**: 3.10 or later installed and available on `PATH`.
- **Platform**: tested in a Powershell terminal.

**Quick Start**
- **Open a PowerShell terminal** and run the game from the src folder:

```powershell
cd src
python main.py
```

**Game Modes**
- **Player vs Player**: enter `a` when prompted.
- **Player vs Computer**: enter `b` when prompted — the computer uses a simple `AimBot` algorithm.

**Controls & Input Format**
- **Coordinates**: enter shots and ship placements using the format `3A`, where `3` is the column (0–9) and `A` is the row (A–J).
- **Ship placement**: enter a ship as a sequence of coordinates separated by spaces.
	- Example for a size-2 ship: `1A 2A`
	- Example for a size-4 ship: `3A 3B 3C 3D`
- **Number and sizes of ships**: each player places four ships with sizes 2, 3, 4 and 5.

**Gameplay Flow**
- At program start you choose mode (`a` or `b`) and enter player names.
- Players place ships in turn (human players manually; computer is auto-placed).
- Players take turns firing at coordinates (always in XY string format). Hits grant another shot; misses pass the turn.
- The match ends when one player has all ships sunk.

**Board Display & Symbols**
- **`~`** (blue): water / untried cell.
- **` O `** (cyan): missed shot.
- **` X `** (red): successful hit.
- **` Ψ `** (green): ship location (shown when printing ship boards).

**Common Issues & Tips**
- If the program reports invalid coordinate input, ensure the coordinate is two characters: a digit `0`–`9` followed by a capital letter `A`–`J`.
- If colors look wrong in your terminal, try a different terminal application that supports ANSI colors (Windows Terminal or PowerShell).

Enjoy the game!