from tic_tac_toe.Tile import Tile


class Board(object):
    __BOARD_SIZE = 3

    def __init__(self):
        self.__plays = []

    def play(self, symbol, x, y):
        if self.__tile_at(x, y) is not None:
            raise Exception('Invalid position')
        self.__plays.append(Tile(x, y, symbol))

    def __tile_at(self, x, y):
        for t in self.__plays:
            if t.x == x and t.y == y:
                return t
        return None

    def a_player_won_on_a_row(self, row):
        return self.__tile_at(row, 0) == self.__tile_at(row, 1) \
               and self.__tile_at(row, 2) == self.__tile_at(row, 1)

    def has_a_winner(self):
        for row in range(self.__BOARD_SIZE):
            if self.__tile_at(row, 0) is not None \
                    and self.__tile_at(row, 1) is not None \
                    and self.__tile_at(row, 2) is not None \
                    and self.a_player_won_on_a_row(row):
                return self.__tile_at(row, 0).symbol

        return None
