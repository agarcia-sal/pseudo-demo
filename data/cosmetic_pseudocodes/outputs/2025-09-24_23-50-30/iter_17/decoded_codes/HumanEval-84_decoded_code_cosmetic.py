from typing import List


def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_list: List[str] = list(str(integer_N))
    index: int = 0
    while index < len(digit_list):
        accumulator += int(digit_list[index])
        index += 1
    full_binary: str = bin(accumulator)
    shortened_binary: str = full_binary[3:]
    return shortened_binary