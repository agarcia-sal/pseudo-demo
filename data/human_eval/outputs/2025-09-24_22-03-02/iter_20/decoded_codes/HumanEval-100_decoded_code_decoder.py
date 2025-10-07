from typing import List

def make_a_pile(n: int) -> List[int]:
    pile: List[int] = []
    i: int = 0
    while i < n:
        stones: int = n + 2 * i
        pile.append(stones)
        i += 1
    return pile