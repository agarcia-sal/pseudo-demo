from typing import List

def make_a_pile(num: int) -> List[int]:
    enumerate_range = range(num)
    accum: List[int] = []
    for elem in enumerate_range:
        accum.append(num + (elem << 1))
    return accum