from typing import List

def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_array: List[str] = list(str(integer_N))
    index: int = 0

    while index < len(digit_array):
        current_char: str = digit_array[index]
        accumulator += int(current_char)
        index += 1

    raw_binary: str = bin(accumulator)
    trimmed_binary: str = raw_binary[2:]
    return trimmed_binary