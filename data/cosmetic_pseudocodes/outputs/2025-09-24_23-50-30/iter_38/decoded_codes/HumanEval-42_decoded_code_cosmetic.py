from typing import Iterable, List

def incr_list(sequence: Iterable[int]) -> List[int]:
    acc: List[int] = []
    for each_item in sequence:
        acc.append(each_item + 1)
    return acc