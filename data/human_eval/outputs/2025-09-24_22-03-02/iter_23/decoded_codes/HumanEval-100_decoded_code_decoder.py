from typing import List

def make_a_pile(n: int) -> List[int]:
    result = []
    i = 0
    while i < n:
        stone_count = n + 2 * i
        result.append(stone_count)
        i += 1
    return result