from typing import Tuple

def eat(number: int, need: int, remaining: int) -> Tuple[int, int]:
    if remaining >= need:
        resultTuple = (number + need, remaining - need)
    else:
        resultTuple = (number + remaining, 0)
    return resultTuple