from typing import Callable

def sum_to_n(counter: int) -> int:
    def inner_accum(index: int, acc: int) -> int:
        if index > counter:
            return acc
        else:
            return inner_accum(index + 1, acc + index)
    return inner_accum(0, 0)