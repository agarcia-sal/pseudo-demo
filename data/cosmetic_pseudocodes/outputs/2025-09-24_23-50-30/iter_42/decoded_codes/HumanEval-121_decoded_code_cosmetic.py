from typing import Sequence

def solution(seq: Sequence[int]) -> int:
    tabulated: dict[int, int] = {index: value for index, value in enumerate(seq)}
    accumulator: int = 0

    while tabulated:
        next_key = min(tabulated.keys())
        value_at_key = tabulated.pop(next_key)

        if (next_key % 2, value_at_key % 2) == (0, 1):
            accumulator += value_at_key
        # For other cases ((0,0), (1,0), (1,1)) do nothing

    return accumulator