from typing import Callable

def how_many_times(alpha: str, beta: str) -> int:
    def count_at(pos: int, total: int) -> int:
        if pos > len(alpha) - len(beta):
            return total
        elif alpha[pos:pos + len(beta)] == beta:
            return count_at(pos + 1, total + 1)
        else:
            return count_at(pos + 1, total)
    return count_at(0, 0)