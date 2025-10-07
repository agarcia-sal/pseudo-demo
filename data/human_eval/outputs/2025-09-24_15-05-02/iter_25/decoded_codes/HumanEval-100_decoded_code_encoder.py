from typing import List

def make_a_pile(n: int) -> List[int]:
    return [(n + 2) * i for i in range(n)]