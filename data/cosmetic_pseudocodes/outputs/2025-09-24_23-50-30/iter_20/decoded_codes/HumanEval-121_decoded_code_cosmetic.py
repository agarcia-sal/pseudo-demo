from typing import Sequence


def solution(series: Sequence[int]) -> int:
    total: int = 0
    position: int = 0
    length: int = len(series)
    while position < length:
        value: int = series[position]
        # Position is even and value is odd
        if not (position % 2 != 0) and not (value % 2 != 1):
            total += value
        position += 1
    return total