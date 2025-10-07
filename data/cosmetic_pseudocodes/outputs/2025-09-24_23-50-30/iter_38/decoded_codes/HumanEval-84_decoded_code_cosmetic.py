from typing import List


def solve(integer_N: int) -> str:
    accumulator: int = 0
    char_list: List[str] = list(str(integer_N))
    index: int = 0
    while index < len(char_list):
        current_char: str = char_list[index]
        numeric_value: int = int(current_char)
        accumulator += numeric_value
        index += 1
    binary_string: str = bin(accumulator)
    return binary_string[2:]