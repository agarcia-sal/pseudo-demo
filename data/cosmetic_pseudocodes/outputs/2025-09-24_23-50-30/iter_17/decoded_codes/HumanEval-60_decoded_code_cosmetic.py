from typing import List

def sum_to_n(param_x: int) -> int:
    container: List[int] = [i for i in range(param_x + 1)]
    accumulator: int = 0
    idx: int = 0
    while idx < len(container):
        accumulator += container[idx]
        idx += 1
    return accumulator