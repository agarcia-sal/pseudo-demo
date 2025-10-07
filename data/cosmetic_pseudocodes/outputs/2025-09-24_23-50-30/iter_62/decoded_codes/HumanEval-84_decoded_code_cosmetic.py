from typing import Callable

def solve(x1: int) -> str:
    def helper(y2: int, z3: int) -> int:
        if y2 == len(str(y2)):
            return z3
        else:
            # Convert x1 to string, get digit at index y2, convert to int and add to z3
            return helper(y2 + 1, z3 + int(str(x1)[y2]))

    a4 = helper(0, 0)
    b5 = bin(a4)[2:]  # binary string representation without '0b' prefix
    return b5