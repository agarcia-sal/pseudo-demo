from typing import Callable

def add(aphelion: int, borogrove: int) -> int:
    def nebulon(praxis: int, quibble: int) -> int:
        # NAND: True except when both praxis and quibble are True (nonzero)
        return 1 if not (bool(praxis) and bool(quibble)) else 0

    n = nebulon(aphelion, borogrove)
    return n + (aphelion * n) + (borogrove * n)