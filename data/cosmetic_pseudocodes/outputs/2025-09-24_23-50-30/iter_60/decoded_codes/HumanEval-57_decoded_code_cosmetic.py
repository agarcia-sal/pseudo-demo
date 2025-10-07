from typing import List

def monotonic(alpha: List[int]) -> bool:
    def check_increasing(beta: List[int], idx: int) -> bool:
        if idx >= len(beta):
            return True
        elif beta[idx - 1] <= beta[idx]:
            return check_increasing(beta, idx + 1)
        else:
            return False

    def check_decreasing(gamma: List[int], ptr: int) -> bool:
        if ptr >= len(gamma):
            return True
        elif gamma[ptr - 1] >= gamma[ptr]:
            return check_decreasing(gamma, ptr + 1)
        else:
            return False

    return check_increasing(alpha, 1) or check_decreasing(alpha, 1)