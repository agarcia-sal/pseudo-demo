from typing import List

def int_to_mini_roman(input_value: int) -> str:
    roman_values: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_syms: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    idx: int = 0
    output_accumulator: str = ""

    while input_value != 0:
        quotient: int = input_value // roman_values[idx]
        input_value %= roman_values[idx]
        output_accumulator += roman_syms[idx] * quotient
        idx += 1

    return output_accumulator.lower()