from typing import List

def make_a_pile(n: int) -> List[int]:
    pile = []
    i = 0
    while i < n:
        stone_count = n + 2 * i
        pile.append(stone_count)
        i += 1
    return pile