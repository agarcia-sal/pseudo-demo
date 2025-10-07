from typing import Dict, Tuple

def int_to_mini_roman(number: int) -> str:
    scale: Tuple[int, ...] = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
    signs: Tuple[str, ...] = ("I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M")
    idx: int = 12
    output: str = ""

    while True:
        if number == 0:
            break
        quotient: int = number // scale[idx]
        number = number % scale[idx]
        while True:
            if quotient == 0:
                break
            output += signs[idx]
            quotient -= 1
        idx -= 1
        if idx < 0:
            break

    return output.lower()