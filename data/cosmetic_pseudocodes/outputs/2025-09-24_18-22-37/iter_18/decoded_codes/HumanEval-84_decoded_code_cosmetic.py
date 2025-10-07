from typing import Union


def solve(puzzle_input: Union[int, str]) -> str:
    total_accumulator: int = 0
    idx: int = 0
    s: str = str(puzzle_input)

    while idx < len(s):
        temp_char: str = s[idx]
        numeric_value: int = int(temp_char)
        total_accumulator += numeric_value
        idx += 1

    full_binary: str = bin(total_accumulator)
    # Strip the '0b' prefix from the binary string
    binary_str: str = full_binary[2:]
    return binary_str