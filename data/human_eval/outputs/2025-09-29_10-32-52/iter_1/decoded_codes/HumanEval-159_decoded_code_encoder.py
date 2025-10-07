from typing import List

def eat(number: int, need: int, remaining: int) -> List[int]:
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]