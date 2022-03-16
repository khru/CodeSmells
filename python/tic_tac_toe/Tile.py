class Tile(object):
    def __init__(self, x: int, y: int, symbol: str):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __eq__(self, other) -> bool:
        return other is not None and self.symbol == other.symbol
