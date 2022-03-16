from tic_tac_toe.Board import Board


class Game(object):

    def __init__(self):
        self._last_player = None
        self._board = Board()

    def play(self, symbol, x, y):
        if self._last_player is None and symbol == 'O':
            raise Exception('Invalid first player')

        if symbol == self._last_player:
            raise Exception('Invalid next player')

        if self._board.tile_at(x, y) is not None:
            raise Exception('Invalid position')

        self._last_player = symbol
        self._board.add_tile_at(symbol, x, y)

    def winner(self):
        return self._board.has_a_winner()
