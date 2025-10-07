from typing import List


def count_upper(str_param: str) -> int:
    accumulator: int = 0
    positions: List[int] = [i for i in range(len(str_param)) if i % 2 == 0]
    for pos in positions:
        if str_param[pos] in {'A', 'E', 'I', 'O', 'U'}:
            accumulator += 1
    return accumulator