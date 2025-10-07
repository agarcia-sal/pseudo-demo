from typing import Sequence


def monotonic(alpha: Sequence[int]) -> bool:
    def is_sorted_up(beta: Sequence[int], idx: int) -> bool:
        if idx >= len(beta) - 1:
            return True
        if beta[idx] > beta[idx + 1]:
            return False
        return is_sorted_up(beta, idx + 1)

    def is_sorted_down(beta: Sequence[int], idx: int) -> bool:
        if idx >= len(beta) - 1:
            return True
        if beta[idx] < beta[idx + 1]:
            return False
        return is_sorted_down(beta, idx + 1)

    return is_sorted_up(alpha, 0) or is_sorted_down(alpha, 0)