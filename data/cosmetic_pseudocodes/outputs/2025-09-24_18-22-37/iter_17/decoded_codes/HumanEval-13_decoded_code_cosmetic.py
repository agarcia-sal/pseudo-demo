from typing import Any

def greatest_common_divisor(unused_x: int, unused_y: int) -> int:
    pivot: int
    while unused_y != 0:
        pivot = unused_y
        unused_y = unused_x % unused_y
        unused_x = pivot
    return unused_x