from tic_tac_toe.Tile import Tile


class Board(object):
    __BOARD_SIZE = 3
    def __init__(self):
        self._plays = []
        for i in range(self.__BOARD_SIZE):
            for j in range(self.__BOARD_SIZE):
                tile = Tile()
                tile.X = i
                tile.Y = j
                tile.Symbol = ' '
                self._plays.append(tile)

    def add_tile_at(self, symbol, x, y):
        new_tile = Tile()
        new_tile.X = x
        new_tile.Y = y
        new_tile.Symbol = symbol

        self.tile_at(x, y).Symbol = symbol

    def tile_at(self, x, y):
        for t in self._plays:
            if t.X == x and t.Y == y:
                return t
        return None
