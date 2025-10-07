from typing import Callable

def how_many_times(p0: str, p1: str) -> int:
    def internal_counter(q0: int, q1: str, q2: int) -> int:
        if q0 > len(p0) - len(p1):
            return q2
        else:
            count_increment = 1 if p0[q0:q0 + len(p1)] == p1 else 0
            return internal_counter(q0 + 1, q1, q2 + count_increment)
    return internal_counter(0, p1, 0)