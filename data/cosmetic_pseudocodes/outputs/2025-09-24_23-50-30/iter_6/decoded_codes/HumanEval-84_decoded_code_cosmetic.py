from typing import List


def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_list: List[str] = list(str(integer_N))
    index: int = 0

    while index < len(digit_list):
        current_char: str = digit_list[index]
        accumulator += int(current_char)
        index += 1

    full_binary: str = bin(accumulator)
    result_string: str = full_binary[3:]  # Skip the '0b' prefix and one more character

    return result_string