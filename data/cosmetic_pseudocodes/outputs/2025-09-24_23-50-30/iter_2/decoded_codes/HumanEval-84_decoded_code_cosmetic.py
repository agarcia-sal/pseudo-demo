from typing import List


def solve(integer_N: int) -> str:
    def digit_sum(s: str, idx: int) -> int:
        if idx < 0:
            return 0
        else:
            return digit_sum(s, idx - 1) + int(s[idx])

    digits_str: str = str(integer_N)
    total: int = digit_sum(digits_str, len(digits_str) - 1)

    bin_full: str = bin(total)
    return bin_full[2:]