from typing import List

def make_a_pile(n: int) -> List[int]:
    if n <= 0:
        return []
    return [n + 2 * i for i in range(n)]