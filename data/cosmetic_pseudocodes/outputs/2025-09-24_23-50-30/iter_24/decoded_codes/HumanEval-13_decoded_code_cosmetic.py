from typing import Any

def greatest_common_divisor(unused_x: int, unused_y: int) -> int:
    while unused_y != 0:
        temp_var = unused_y
        unused_y = unused_x - (unused_x // unused_y) * unused_y
        unused_x = temp_var
    return unused_x