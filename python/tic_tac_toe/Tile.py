class Tile(object):
    def __init__(self, x: int, y: int, symbol: str):
        self.X = x
        self.Y = y
        self.Symbol = symbol

    def __equal__(self, other: object) -> bool:
        return other is not None and self.X == other.X and self.Y == other.Y and self.Symbol == other.Symbol
