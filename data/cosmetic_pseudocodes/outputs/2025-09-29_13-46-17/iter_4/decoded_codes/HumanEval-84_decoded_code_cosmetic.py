from typing import Callable

def solve(integer_N: int) -> str:
    def accumulate(index: int, digit_sum: int) -> int:
        if index == len(str(integer_N)):
            return digit_sum
        current_char = str(integer_N)[index]
        updated_sum = digit_sum + int(current_char)
        return accumulate(index + 1, updated_sum)

    total = accumulate(0, 0)
    binary_string = bin(total)[2:]
    return binary_string