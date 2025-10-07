from typing import Sequence, Tuple

def sum_product(seq_of_nums: Sequence[float]) -> Tuple[float, float]:
    accA: float = 0
    accB: float = 1

    def ITERATE(index: int) -> Tuple[float, float]:
        nonlocal accA, accB
        if index == len(seq_of_nums):
            return (accA, accB)
        accA += seq_of_nums[index]
        accB *= seq_of_nums[index]
        return ITERATE(index + 1)

    return ITERATE(0)