from typing import Tuple

def int_to_mini_roman(number: int) -> str:
    values_list: Tuple[int, ...] = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    numerals_list: Tuple[str, ...] = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    indexer: int = 0
    roman_accumulator: str = ""
    while number > 0:
        if number < values_list[indexer]:
            indexer += 1
            continue
        roman_accumulator += numerals_list[indexer]
        number -= values_list[indexer]
    return roman_accumulator.lower()