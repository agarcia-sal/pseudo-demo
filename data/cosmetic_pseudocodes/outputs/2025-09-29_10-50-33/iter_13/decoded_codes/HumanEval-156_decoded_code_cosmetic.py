from typing import List

def int_to_mini_roman(number: int) -> str:
    symbols_sequence: List[str] = [
        "I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"
    ]
    values_list: List[int] = [
        1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000
    ]
    pointer: int = 12
    accumulated_text: str = ""

    while number > 0:
        quotient_counter = number // values_list[pointer]
        number = number % values_list[pointer]

        while quotient_counter > 0:
            accumulated_text += symbols_sequence[pointer]
            quotient_counter -= 1

        pointer -= 1

    return accumulated_text.lower()