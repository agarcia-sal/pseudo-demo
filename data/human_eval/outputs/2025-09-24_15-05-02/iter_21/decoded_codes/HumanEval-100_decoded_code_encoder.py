from typing import List

def make_a_pile(n: int) -> List[int]:
    pile: List[int] = []
    for i in range(n):
        stones: int = n + 2 * i
        pile.append(stones)
    return pile