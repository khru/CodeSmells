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

    def a_player_won_on_the_first_row(self):
        return self._board.tile_at(0, 0) == self._board.tile_at(0, 1) \
                and self._board.tile_at(0, 2) == self._board.tile_at(0, 1)

    def a_player_won_on_the_second_row(self):
        return self._board.tile_at(1, 0) == self._board.tile_at(1, 1) \
                    and self._board.tile_at(1, 2) == self._board.tile_at(1, 1)

    def a_player_won_on_the_third_row(self):
        return self._board.tile_at(2, 0) == self._board.tile_at(2, 1) \
                    and self._board.tile_at(2, 2) == self._board.tile_at(2, 1)

    def winner(self):
        # if the positions in first row are taken
        if self._board.tile_at(0, 0) is not None \
                and self._board.tile_at(0, 1) is not None \
                and self._board.tile_at(0, 2) is not None:
            # if first row is full with same symbol
            if self.a_player_won_on_the_first_row():
                return self._board.tile_at(0, 0).symbol

        # if the positions in second row are taken
        if self._board.tile_at(1, 0) is not None \
                and self._board.tile_at(1, 1) is not None \
                and self._board.tile_at(1, 2) is not None:
            # if first second is full with same symbol
            if self.a_player_won_on_the_second_row():
                return self._board.tile_at(1, 0).symbol

        # if the positions in third row are taken
        if self._board.tile_at(2, 0) is not None \
                and self._board.tile_at(2, 1) is not None \
                and self._board.tile_at(2, 2) is not None:
            # if first row is third with same symbol
            if self.a_player_won_on_the_third_row():
                return self._board.tile_at(2, 0).symbol

        return None
