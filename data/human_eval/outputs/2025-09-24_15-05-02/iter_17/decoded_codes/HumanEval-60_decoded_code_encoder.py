from typing import SupportsIndex

def sum_to_n(n: SupportsIndex) -> int:
    value = n.__index__()
    if value < 0:
        return 0
    return value * (value + 1) // 2