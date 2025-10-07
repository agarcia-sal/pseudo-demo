from typing import List

def int_to_mini_roman(value: int) -> str:
    digits_list: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters_list: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    idx: int = 0
    output: str = ""
    while value != 0:
        count: int = value // digits_list[idx]
        value %= digits_list[idx]
        output += letters_list[idx] * count
        idx += 1
    return output.lower()