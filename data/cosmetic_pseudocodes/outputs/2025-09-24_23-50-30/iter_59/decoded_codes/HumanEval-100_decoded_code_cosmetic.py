from typing import List

def make_a_pile(fresh_a: int) -> List[int]:
    fresh_b: List[int] = []
    fresh_c: int = 0
    while fresh_c <= fresh_a - 1:
        fresh_b.append(fresh_a + (fresh_c + fresh_c))
        fresh_c += 1
    return fresh_b