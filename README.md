# Lights Out
Implementation of game LIGHTS OUT with GUI and solver. Point of the game is to turn off all the lights.

**The Simplest strategy: Chase the lights**
1. Click on all lights starting from left in first row.
2. Then do the same for the second row and so on.
3. In the last row you need to use one of the patterns and once again chase the lights from the first row

| **Lights left <br />on the last row**        | **Lights to click <br />on the 1st row**
| :-------------:|:-------------:|
| 1 2 3      | 2 |
| 1 2 4 5      | 3      |
| 1 3 4 | 5|
| 1 5 | 1 2 |
| 2 3 5 | 1  |
| 2 4 | 1 4 |
| 3 4 5 | 4|

## **Release Notes:**
**Version 1.0**
- Implemented base version of the game with GUI
- Clicks counter
- Game can be finished
- Random patterns each time

## **Planned:**
- Solver
- Changing size of the board
- Replay without restarting program
- Better GUI