from typing import List


def int_to_mini_roman(input_value: int) -> str:
    values: List[int] = [0x3E8, 0x384, 0x1F4, 0x190, 0x64, 0x5A, 0x28, 0x14, 0xA, 9, 5, 4, 1]
    symbols: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    cursor: int = 0
    output_accum: str = ""
    while input_value > 0:
        if input_value >= values[cursor]:
            output_accum += symbols[cursor]
            input_value -= values[cursor]
        else:
            cursor += 1
    return output_accum.lower()