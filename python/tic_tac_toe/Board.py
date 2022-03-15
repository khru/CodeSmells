from tic_tac_toe.Tile import Tile


class Board(object):
    def __init__(self):
        self._plays = []

    def add_tile_at(self, symbol, x, y):
        self._plays.append(Tile(x, y, symbol))

    def tile_at(self, x, y):
        for t in self._plays:
            if t.X == x and t.Y == y:
                return t
        return None
