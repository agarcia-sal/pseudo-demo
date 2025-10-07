from typing import Callable

def solve(qwop: object) -> str:
    def helper_function(xyz: str, acc: int) -> int:
        if not xyz:
            return acc
        return helper_function(xyz[1:], acc + int(xyz[0]))

    temp_str: str = str(qwop)
    total_sum: int = helper_function(temp_str, 0)
    binary_str: str = bin(total_sum)[2:]  # slice off '0b' prefix
    return binary_str