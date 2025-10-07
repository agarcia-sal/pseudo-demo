from typing import List


def add_elements(list_of_ints: List[int], num_limit: int) -> int:
    acc: int = 0
    idx: int = 0
    while idx < num_limit and idx < len(list_of_ints):
        if len(str(list_of_ints[idx])) <= 2:
            acc += list_of_ints[idx]
        idx += 1
    return acc