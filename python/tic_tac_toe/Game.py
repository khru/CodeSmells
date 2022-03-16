from tic_tac_toe.Board import Board


class Game(object):

    def __init__(self):
        self._last_player = None
        self._board = Board()

    def play(self, symbol, x, y):
        # if first move
        if self._last_player is None and symbol == 'O':
            raise Exception('Invalid first player')

        if symbol == self._last_player:
            raise Exception('Invalid next player')

        if self._board.tile_at(x, y) is not None:
            raise Exception('Invalid position')

        # update game state
        self._last_player = symbol
        self._board.add_tile_at(symbol, x, y)

    def a_player_won_on_a_row(self, row):
        return self._board.tile_at(row, 0) == self._board.tile_at(row, 1) \
                and self._board.tile_at(row, 2) == self._board.tile_at(row, 1)

    def winner(self):
        # if the positions in first row are taken
        for row in range(3):
            if self._board.tile_at(row, 0) is not None \
                    and self._board.tile_at(row, 1) is not None \
                    and self._board.tile_at(row, 2) is not None \
                    and self.a_player_won_on_a_row(row):
                return self._board.tile_at(row, 0).symbol

        return None
