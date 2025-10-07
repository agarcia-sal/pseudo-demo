from typing import Callable

def largest_divisor(integer_n: int) -> int:
    def rec_search(entry_x: int, entry_y: int) -> int:
        if entry_y % entry_x == 0:
            return entry_x
        else:
            return rec_search(entry_x - 1, entry_y)
    return rec_search(integer_n - 1, integer_n)