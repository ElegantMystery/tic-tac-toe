from player import Point, Player
from board import Game, Move
from minimax import MiniMaxAgent
from alphabeta import AlphaBetaAgent
from mcts import MCTSAgent
from randombot import RandomBot
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
    gamenum = 100
    bot1_win = 0
    bot1_draw = 0
    bot1_loss = 0
    while gamenum > 0:
        game = Game.new_game()
        bot1 = AlphaBetaAgent()
        bot2 = MiniMaxAgent()
        if gamenum > gamenum // 2:
            game.next_player = Player.x
        else:
            game.next_player = Player.o
        while not game.is_over():
            if game.next_player == Player.x:
                move = bot1.move(game)
            else:
                move = bot2.move(game)
            game = game.apply_move(move)
        winner = game.winner()
        if winner is None:
            print("It is a draw.")
            bot1_draw += 1
        else:
            if winner == Player.x:
                bot1_win += 1
                print("Bot1 Win!")
            else:
                bot1_loss += 1
                print("Bot1 Lose")
        gamenum -= 1
    print("bot1 win number: " + str(bot1_win))
    print("bot1 loss number: " + str(bot1_loss))
    print("bot1 draw number: " + str(bot1_draw))
        

if __name__ == "__main__":
    main()    
