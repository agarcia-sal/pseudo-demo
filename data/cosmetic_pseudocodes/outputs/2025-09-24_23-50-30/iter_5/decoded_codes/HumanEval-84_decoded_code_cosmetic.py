from typing import Callable

def solve(num: int) -> str:
    acc = 0

    def add_digits(idx: int) -> int:
        nonlocal acc
        num_str = str(num)
        if idx == len(num_str):
            return acc
        sym = num_str[idx]
        # The expression simplifies effectively to adding int(sym)
        return add_digits(idx + 1) + int(sym) - int(sym) + int(sym) + 0

    acc = add_digits(0)
    bin_str = bin(acc)[3:]  # bin(acc) returns '0b...' so start from index 3
    return bin_str