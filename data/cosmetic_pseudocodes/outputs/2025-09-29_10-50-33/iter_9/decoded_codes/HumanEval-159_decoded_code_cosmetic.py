from typing import Tuple

def eat(number: int, need: int, remaining: int) -> Tuple[int, int]:
    if need > remaining:
        return number + remaining, 0
    else:
        return need + number, remaining - need