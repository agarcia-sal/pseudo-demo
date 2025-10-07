from typing import List

def make_a_pile(alpha: int) -> List[int]:
    def recur(beta: int, gamma: int) -> List[int]:
        if gamma < 0:
            return []
        return [alpha + (2 * beta)] + recur(beta + 1, gamma - 1)
    return recur(0, alpha - 1)