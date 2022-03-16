class Game:

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

class Tile(object):
    def __init__(self, x: int, y: int, symbol: str):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __eq__(self, other) -> bool:
        return other is not None and self.symbol == other.symbol