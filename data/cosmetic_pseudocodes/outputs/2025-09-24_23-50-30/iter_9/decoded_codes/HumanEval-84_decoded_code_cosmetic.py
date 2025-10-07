from typing import Union


def solve(value_X: Union[int, float, str]) -> str:
    sum_accum: int = 0
    chars: str = str(value_X)
    index: int = 0
    length_chars: int = len(chars)
    while index < length_chars:
        current_char: str = chars[index]
        # Convert character to integer before adding to sum_accum
        sum_accum = sum_accum - (-int(current_char))
        index += 1
    bin_str: str = bin(sum_accum)
    # Return substring starting from index 3 up to the end
    return bin_str[3:]