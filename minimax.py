import random
import enum 
from board import Game
import copy
from time import sleep

class GameResult(enum.Enum):
   win = 3
   draw = 2
   loss = 1

def opposite(game_result):
         if game_result == GameResult.win:
            return GameResult.loss
         elif game_result == GameResult.loss:
            return GameResult.win 
         else:
            return GameResult.draw

def best_move(game):
   if game.is_over():
      if game.winner() == game.next_player:
         return GameResult.win 
      elif game.winner() == game.next_player.other:
         return GameResult.loss
      else:
         return GameResult.draw 
   else:
      best_result = GameResult.loss
      for move in game.potential_moves():
         next_state = game.apply_move(move)
         opponent_move = best_move(next_state)
         my_move = opposite(opponent_move)
         if my_move.value > best_result.value:
            best_result = my_move
      return best_result 

class MiniMaxAgent():
   #Minimax Algorithms
   
   def move(self, game):
      '''
      def find_winning_move(game):
         for move in game.potential_moves():
            next_state = game.apply_move(move)
            if next_state.is_over() and next_state.winner() == game.next_player:
               return move 
         return None
      
      def find_losing_move(game): # return moves which will not lose
         potential_moves = []
         next_board = copy.deepcopy(game.board)
         for move in game.potential_moves():
            next_state = Game(next_board, game.next_player.other, move)
            if next_state.is_over() and next_state.winner() == game.next_player.other:
               print(str(move.point.row) + ' ' + str(move.point.col) + 'is bad move')
               sleep(2)
               continue 
            else:
               potential_moves.append(move)
         return potential_moves
      '''

      winning_moves, draw_moves, loss_moves = [], [], []
      
      for move in game.potential_moves():
         next_state = game.apply_move(move)
         opponent_move = best_move(next_state)
         my_move = opposite(opponent_move)
         if my_move == GameResult.win:
            return move
            winning_moves.append(move)
         elif my_move == GameResult.draw:
            draw_moves.append(move)
         else:
            loss_moves.append(move)
      
      if winning_moves:
         '''
         print("winning!")
         sleep(2)
         '''
         return random.choice(winning_moves)
      elif draw_moves:
         '''
         print("draw!")
         sleep(2)
         '''
         return random.choice(draw_moves)
      else:
         '''
         print("losing!")
         sleep(2)
         '''
         return random.choice(loss_moves)
