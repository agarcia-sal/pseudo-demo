from typing import List

def int_to_mini_roman(number: int) -> str:
    symbols: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result: List[str] = []
    index: int = 0

    while number > 0:
        while number >= values[index]:
            result.append(symbols[index])
            number -= values[index]
        index += 1

    return "".join(result).lower()