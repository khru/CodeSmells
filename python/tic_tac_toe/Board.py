from tic_tac_toe.Tile import Tile


class Board(object):
    def __init__(self):
        self._plays = []

    def add_tile_at(self, symbol, x, y):
        self._plays.append(Tile(x, y, symbol))

    def tile_at(self, x, y):
        for t in self._plays:
            if t.x == x and t.y == y:
                return t
        return None

    def a_player_won_on_a_row(self, row):
        return self.tile_at(row, 0) == self.tile_at(row, 1) \
               and self.tile_at(row, 2) == self.tile_at(row, 1)

    def has_a_winner(self):
        for row in range(3):
            if self.tile_at(row, 0) is not None \
                    and self.tile_at(row, 1) is not None \
                    and self.tile_at(row, 2) is not None \
                    and self.a_player_won_on_a_row(row):
                return self.tile_at(row, 0).symbol

        return None
