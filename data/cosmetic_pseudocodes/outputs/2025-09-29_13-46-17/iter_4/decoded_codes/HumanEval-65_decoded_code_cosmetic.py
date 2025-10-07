from typing import Union


def circular_shift(integer_x: int, integer_shift: int) -> str:
    digit_chars = str(integer_x)
    length = len(digit_chars)
    if integer_shift > length:
        return digit_chars[::-1]  # reverse string if shift exceeds length
    split_point = length - integer_shift
    part_end = digit_chars[split_point:]
    part_start = digit_chars[:split_point]
    return part_end + part_start