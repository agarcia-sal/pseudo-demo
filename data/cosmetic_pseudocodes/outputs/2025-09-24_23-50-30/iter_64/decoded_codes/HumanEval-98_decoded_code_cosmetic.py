from typing import Callable

def count_upper(alpha: str) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position >= len(alpha):
            return accumulator
        if alpha[position] in {"A", "E", "I", "O", "U"}:
            return helper(position + 2, accumulator + 1)
        return helper(position + 2, accumulator)
    return helper(0, 0)