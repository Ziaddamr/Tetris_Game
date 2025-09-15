from renderer import Renderer
import time
import gameplay
from utilities import clear
from utilities import hide_cursor
import msvcrt
from block import Block
import validation


class Game():
    Score = dict(score=0)

    @classmethod
    def start(cls):
        clear()
        hide_cursor()
        print(
            "===========================WELCOME TO TETRIS GAME===========================")
        print("\n\n===========================Press 1 to play==================================")
        print("\n\n===========================Press 2 for leaderboard===========================")
        choice = msvcrt.getch()
        if choice == b"1":
            renderer = Renderer()
            frame = renderer.generateFrame()
            while True:
                x_coordinate, y_coordinate = renderer.WIDTH//2, renderer.HEIGHT//11
                should_continue = True
                clear()
                validation.is_row_full(frame, Game.Score, renderer)
                block = Block()
                renderer.drawBlock(frame, block, x_coordinate, y_coordinate,
                                   block.width, block.height)
                renderer.drawFrame(frame, Game.Score)
                if validation.is_game_over(frame, block, x_coordinate, y_coordinate, block.width, block.height):
                    time.sleep(1)
                    clear()
                    break
                while should_continue:
                    time.sleep(0.05)
                    start = time.time()
                    while time.time() - start < 0.05:
                        if msvcrt.kbhit():
                            key = msvcrt.getch()
                            x_coordinate, y_coordinate, block, should_continue = gameplay.movement(
                                frame, block, x_coordinate, y_coordinate, Game.Score, renderer, key)

                        else:
                            x_coordinate, y_coordinate, block, should_continue = gameplay.movement(
                                frame, block, x_coordinate, y_coordinate, Game.Score, renderer,  b"")
        elif choice == b"2":
            pass
