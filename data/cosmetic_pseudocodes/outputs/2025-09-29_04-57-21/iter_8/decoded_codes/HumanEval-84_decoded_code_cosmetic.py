from typing import Union

def solve(integer_N: Union[int, str]) -> str:
    total: int = 0
    digits = list(str(integer_N))
    index: int = 0
    while index < len(digits):
        current_char = digits[index]
        total += int(current_char)
        index += 1
    binary_str = bin(total)
    return binary_str[2:]