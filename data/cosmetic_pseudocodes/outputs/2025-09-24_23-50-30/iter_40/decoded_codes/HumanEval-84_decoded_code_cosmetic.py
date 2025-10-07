from typing import List


def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_array: List[str] = list(str(integer_N))
    index: int = 0
    while index < len(digit_array):
        accumulator += int(digit_array[index])
        index += 1
    full_binary: str = bin(accumulator)
    result: str = full_binary[2:]
    return result