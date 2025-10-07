from typing import List, Optional

def pluck(collection: List[int]) -> List[int]:
    idx: int = 0
    evens: List[int] = []
    res: List[int] = []

    while idx < len(collection):
        if collection[idx] % 2 == 0:
            evens.append(collection[idx])
        idx += 1

    if len(evens) == 0:
        return []

    min_val: int = evens[0]
    i: int = 1
    while i < len(evens):
        if min_val > evens[i]:
            min_val = evens[i]
        i += 1

    pos: int = 0
    while pos < len(collection):
        if collection[pos] == min_val:
            break
        pos += 1

    res = [min_val, pos]

    return res