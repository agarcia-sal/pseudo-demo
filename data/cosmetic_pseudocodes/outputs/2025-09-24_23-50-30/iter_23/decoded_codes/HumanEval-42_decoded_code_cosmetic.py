from typing import List

def incr_list(container: List[int]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index < len(container):
        accumulator.append(container[index] + 1)
        index += 1
    return accumulator