'''
    ysh99226@gmail.com Shanghua Yang
    lyl1021@bu.edu Yilin Li
    xyuhu@bu.edu Xiangyu Hu
'''

from player import Point, Player
from board import Game, Move
from minimax import MiniMaxAgent
from alphabeta import AlphaBetaAgent
from mcts import MCTSAgent
import os
def print_board(board):
    for row in range(1,4):
        res = []
        for col in range(1,4):
            x = board.get(Point(row,col))
            if x == Player.x:
                res.append("X")
            elif x == Player.o:
                res.append("O")
            else:
                res.append('-')
        print('%s' % ' | '.join(res))
        if row != 3:
            print("---------")

def main():
    game = Game.new_game()
    human = Player.x
    bot = MCTSAgent(30000)
    os.system('clear')
    while True:
        cOrder = input("Do you want to go first? Y/N: ")
        if cOrder == 'Y' or cOrder == 'y':
            game.next_player = human
            break
        elif cOrder == 'N' or cOrder =='n':
            game.next_player = Player.o
            break 
        else:
            print("Wrong input, Try again")
    while not game.is_over():
        print_board(game.board)
        if game.next_player == human:
            while True:
                try:
                    human_row, human_col = input('Enter your move: ').split()
                    break
                except (ValueError):
                    print("Invalid Input, Try again")
            point = Point(int(human_row), int(human_col))
            move = Move(point)
        else:
            move = bot.move(game)
        game = game.apply_move(move)
        os.system('clear')
    print_board(game.board)
    winner = game.winner()
    if winner is None:
        print("It is a draw.")
    else:
        if winner == human:
            print("You Win!")
        else:
            print("You Lose")

if __name__ == "__main__":
    main()    
