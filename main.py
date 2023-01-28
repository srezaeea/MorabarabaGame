import random

from board import *
from robot import Robot
from node import Node



game_is_on = True
if input("if you enter 1 bot will start the game you will start the game if you enter other numbers :") == '1':
    start_by_user = False
else:
    start_by_user = True

board = Board(start_by_user)
robot = Robot(GAME_LEVEL)
board.showBoard()

i = -3
while game_is_on:
    if board.turn_is_user:
        print(f"reminded indexes = {board.indexes}")
        user_selected = board.add_point(int(input("please select place :")), True)
        if not user_selected :
            print("invalid input!!!")
        else: board.turn_is_user = False
    else:
        print("please wait bot is thinking ... 😊")
        node = Node(None, None, None, None, -1)
        robot_selected_node = robot.minimax(node, True, board.states, board.indexes)
        board.add_point(robot_selected_node.index,False)
        board.turn_is_user = True
        i += 1 # i is the step of increasing depth search

    if board.board_is_full():
        if board.robot_grade > board.user_grade :
            print("game is done . you lose")
        elif board.robot_grade == board.user_grade :
            print("game is done . draw")
        else:
            print("game is done. Congregation You won 😊")
        game_is_on = False
