from typing import Protocol, Union


class Interval(Protocol):
    def at(self, index: int) -> int:
        ...


def intersection(interval1: Interval, interval2: Interval) -> str:
    def is_prime(alpha: int) -> bool:
        if alpha in (0, 1):
            return False
        if alpha == 2:
            return True
        for beta in range(2, alpha):
            if alpha % beta == 0:
                return False
        return True

    x: int = interval1.at(0)
    y: int = interval2.at(0)
    start_val: int = x if x > y else y

    p: int = interval1.at(1)
    q: int = interval2.at(1)
    end_val: int = p if p < q else q

    diff: int = end_val - start_val

    if not (diff > 0):
        return "NO"

    return "YES" if is_prime(diff) else "NO"