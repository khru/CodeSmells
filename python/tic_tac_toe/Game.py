from tic_tac_toe.Board import Board


class Game(object):

    def __init__(self):
        self._lastSymbol = ' '
        self._board = Board()

    def play(self, symbol, x, y):
        # if first move
        if self._lastSymbol == ' ':
            # if player is X
            if symbol == 'O':
                raise Exception('Invalid first player')
        # if not first move but player repeated
        elif symbol == self._lastSymbol:
            raise Exception('Invalid next player')
        # if not first move but play on an already played tile
        elif self._board.tile_at(x, y).Symbol != ' ':

            raise Exception('Invalid position')

        # update game state
        self._lastSymbol = symbol
        self._board.add_tile_at(symbol, x, y)

    def winner(self):
        # if the positions in first row are taken
        if self._board.tile_at(0, 0).Symbol != ' ' \
                and self._board.tile_at(0, 1).Symbol != ' ' \
                and self._board.tile_at(0, 2).Symbol != ' ':
            # if first row is full with same symbol
            if self._board.tile_at(0, 0).Symbol == self._board.tile_at(0, 1).Symbol \
                    and self._board.tile_at(0, 2).Symbol == self._board.tile_at(0, 1).Symbol:
                return self._board.tile_at(0, 0).Symbol

        # if the positions in first row are taken
        if self._board.tile_at(1, 0).Symbol != ' ' \
                and self._board.tile_at(1, 1).Symbol != ' ' \
                and self._board.tile_at(1, 2).Symbol != ' ':
            # if first row is full with same symbol
            if self._board.tile_at(1, 0).Symbol == self._board.tile_at(1, 1).Symbol \
                    and self._board.tile_at(1, 2).Symbol == self._board.tile_at(1, 1).Symbol:
                return self._board.tile_at(1, 0).Symbol

        # if the positions in first row are taken
        if self._board.tile_at(2, 0).Symbol != ' ' \
                and self._board.tile_at(2, 1).Symbol != ' ' \
                and self._board.tile_at(2, 2).Symbol != ' ':
            # if first row is full with same symbol
            if self._board.tile_at(2, 0).Symbol == self._board.tile_at(2, 1).Symbol \
                    and self._board.tile_at(2, 2).Symbol == self._board.tile_at(2, 1).Symbol:
                return self._board.tile_at(2, 0).Symbol

        return ' '
