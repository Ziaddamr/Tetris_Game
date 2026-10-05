🧱 Python Tetris

A modular, classic Tetris clone built entirely from scratch using Python. This project emphasizes clean architecture by separating game logic, rendering, and validation into distinct modules.

📂 Project Structure

The codebase is organized into focused, single-responsibility files:

main.py: The entry point of the application. Handles initialization and kicks off the main loop.

game.py & gameplay.py: Manages the core game state, loop, and overall gameplay mechanics.

block.py: Defines the properties and behaviors of the Tetromino pieces, including shapes, coordinates, and rotation states.

renderer.py: Handles all visual output, drawing the matrix grid, active blocks, and any UI elements to the screen.

utilities.py: Contains shared helper functions to cleanly encapsulate logic used by both the game and renderer modules.

validation.py: Responsible for strict collision detection, boundary checking, and termination conditions (e.g., terminating the game immediately when a newly spawned block is immobile).

✨ Features

Classic Tetris block-stacking and line-clearing mechanics.

Modular design without heavy reliance on massive game engine frameworks.

Accurate collision detection to prevent blocks from overlapping or moving out of bounds.

Proper game over handling when the grid tops out.
