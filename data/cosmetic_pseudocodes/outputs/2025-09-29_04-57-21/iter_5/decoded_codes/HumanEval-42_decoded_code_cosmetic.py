from typing import Iterable, List

def incr_list(sequence: Iterable[int]) -> List[int]:
    accumulator: List[int] = []
    for item in sequence:
        accumulator.append(item + 1)
    return accumulator