from player import Player, Point
import copy
from time import sleep
__all__ = [
    'Board',
    'Game',
    'Move',
]


BOARD_SIZE = 3
ROWS = COLS = tuple(range(1, BOARD_SIZE + 1))


class Board:
    def __init__(self): 
        self.board = {}
    
    def place(self, player, point):
        if not self.is_on_board(point) or self.board.get(point) is not None:
            print("Illegal Move!")
            sleep(2)
            return False 
        self.board[point] = player
        return True

    
    def is_on_board(self, point):
        return 1 <= int(point.row) <= 3 and 1 <= int(point.col) <=3 
    
    def get(self, point):
        return self.board.get(point)


class Move:
    def __init__(self, point):
        self.point = point

class Game:
    def __init__(self, board, next_player, move):
        self.board = board
        self.next_player = next_player 
        self.last_move = move 
    
    def apply_move(self,move):
        next_board = copy.deepcopy(self.board)
        if next_board.place(self.next_player, move.point):
            return Game(next_board, self.next_player.other, move)
        else: 
            return Game(self.board, self.next_player, move)
    
    def new_game():
        board = Board()
        return Game(board, Player.x, None)
    
    def is_valid_move(self, move):
        return self.board.get(move.point) is None and not self.is_over()
    
    def potential_moves(self):
        moves= []
        for row in ROWS:
            for col in COLS:
                move = Move(Point(row,col))
                if self.is_valid_move(move):
                    moves.append(move)
        return moves 
    
    def is_over(self):
        if self.check_win(Player.x) or self.check_win(Player.o):
            return True
        for row in ROWS:
            for col in COLS:
                if self.board.get(Point(row, col)) is None:
                    return False
        return True 
    
    def check_win(self, player):
        for col in COLS:
            if all(self.board.get(Point(row, col)) == player for row in ROWS):
                return True
        for row in ROWS:
            if all(self.board.get(Point(row, col)) == player for col in COLS):
                return True
        if self.board.get(Point(1,1)) == self.board.get(Point(2,2)) == self.board.get(Point(3,3)) == player:
            return True
        if self.board.get(Point(1,3)) == self.board.get(Point(2,2)) == self.board.get(Point(3,1)) == player:
            return True
        return False 

    def winner(self):
        if self.check_win(Player.x):
            return Player.x
        if self.check_win(Player.o):
            return Player.o
        return None  
       



    
