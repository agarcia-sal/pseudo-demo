from typing import Callable

def solve(integer_N: int) -> str:
    def sumDigits(num: int, idx: int, total: int) -> int:
        if idx == len(str(num)):
            return total
        return sumDigits(num, idx + 1, total + int(str(num)[idx]))

    total_sum = sumDigits(integer_N, 0, 0)
    bin_repr = bin(total_sum)
    result = bin_repr[3:]  # substring from index 3 to end
    return result