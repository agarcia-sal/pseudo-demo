from typing import Tuple


def int_to_mini_roman(value: int) -> str:
    symbols: Tuple[str, ...] = ("I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M")
    values: Tuple[int, ...] = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
    idx: int = 12

    def append_symbols(count: int, index: int, acc: str) -> str:
        if count <= 0:
            return acc
        return append_symbols(count - 1, index, acc + symbols[index])

    result_string: str = ""

    while value > 0:
        quotient = value // values[idx]
        value -= values[idx] * quotient
        result_string = append_symbols(quotient, idx, result_string)
        idx -= 1

    return result_string.lower()