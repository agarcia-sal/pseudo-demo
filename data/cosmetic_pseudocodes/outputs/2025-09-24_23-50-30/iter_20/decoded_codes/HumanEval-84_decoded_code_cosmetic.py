from typing import List


def solve(integer_N: int) -> str:
    digit_chars: List[str] = list(str(integer_N))

    def helper(index: int) -> int:
        if index >= len(digit_chars):
            return 0
        return int(digit_chars[index]) + helper(index + 1)

    accumulator: int = helper(0)
    binary_string: str = bin(accumulator)
    return binary_string[2:]