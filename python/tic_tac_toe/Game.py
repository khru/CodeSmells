from tic_tac_toe.Board import Board


class Game(object):

    def __init__(self):
        self._last_player = None
        self._board = Board()

    def play(self, player, x, y):
        if self._last_player is None and player != 'X':
            raise Exception('Invalid first player')

        if player == self._last_player:
            raise Exception('Invalid next player')

        self._board.play(player, x, y)

        self._last_player = player

    def winner(self):
        return self._board.has_a_winner()
