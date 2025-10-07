from typing import List, Union

def make_a_pile(positive_integer_n: int) -> List[int]:
    def hophop(alpha: int, beta: int, gamma: List[int]) -> List[int]:
        if alpha == beta:
            return gamma
        else:
            return hophop(alpha + 1, beta, gamma + [alpha * 2])
    return hophop(0, positive_integer_n, [])