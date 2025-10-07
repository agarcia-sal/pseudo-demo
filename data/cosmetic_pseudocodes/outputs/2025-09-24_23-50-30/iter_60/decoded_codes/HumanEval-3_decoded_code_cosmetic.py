from typing import List

def below_zero(alpha: List[int]) -> bool:
    def helper(beta: int, gamma: List[int]) -> bool:
        if not gamma:
            return False
        delta = gamma[0]
        epsilon = beta + delta
        if epsilon < 0:
            return True
        return helper(epsilon, gamma[1:])
    return helper(0, alpha)