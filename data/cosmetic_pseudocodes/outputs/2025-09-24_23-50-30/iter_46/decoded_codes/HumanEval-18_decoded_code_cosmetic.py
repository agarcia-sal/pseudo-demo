from typing import Callable

def how_many_times(alpha: str, beta: str) -> int:
    def count_matches(delta: int) -> int:
        if delta >= len(alpha) - len(beta) + 1:
            return 0
        if alpha[delta:delta + len(beta)] == beta:
            return 1 + count_matches(delta + 1)
        return count_matches(delta + 1)

    return count_matches(0)