from typing import List

def int_to_mini_roman(number: int) -> str:
    numeral_values: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numeral_symbols: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    position_marker: int = 0
    constructed_text: str = ""

    while number > 0:
        quotient_count: int = number // numeral_values[position_marker]
        number -= quotient_count * numeral_values[position_marker]

        while quotient_count > 0:
            constructed_text += numeral_symbols[position_marker]
            quotient_count -= 1

        position_marker += 1

    return constructed_text.lower()