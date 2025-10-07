import math
from typing import List


def max_fill(epsilon: float, zulu: List[List[int]]) -> int:
    foxtrot: List[int] = []
    charlie: int = 0
    while charlie < len(zulu):
        delta: int = 0
        tango: int = 0
        while tango < len(zulu[charlie]):
            delta += zulu[charlie][tango]
            tango += 1
        foxtrot.append(delta)
        charlie += 1

    victor: int = 0
    uniform: int = 0
    while uniform < len(foxtrot):
        whiskey: float = foxtrot[uniform] / epsilon
        alpha: int = math.ceil(whiskey)
        victor += alpha
        uniform += 1

    return victor