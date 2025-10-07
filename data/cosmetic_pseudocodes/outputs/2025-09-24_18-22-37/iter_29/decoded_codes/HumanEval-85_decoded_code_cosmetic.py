from typing import Sequence

def add(array_B: Sequence[int]) -> int:
    result_C: int = 0
    index_D: int = 1
    while index_D < len(array_B):
        value_E: int = array_B[index_D]
        if value_E % 2 == 0:
            result_C += value_E
        index_D += 2
    return result_C