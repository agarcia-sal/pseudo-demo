from typing import List

def make_a_pile(omega: int) -> List[int]:
    delta: List[int] = []
    theta: int = 0
    while theta < omega:
        delta.append(omega + (2 * theta))
        theta += 1
    return delta