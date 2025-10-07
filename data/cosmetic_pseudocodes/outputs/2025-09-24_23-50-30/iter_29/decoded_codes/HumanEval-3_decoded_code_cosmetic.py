from typing import Iterable


def below_zero(set_of_ops: Iterable[int]) -> bool:
    accumulator: int = 0
    for op in set_of_ops:
        accumulator += op
        if accumulator < 0:
            return True
    return False