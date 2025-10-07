from typing import List


def int_to_mini_roman(value: int) -> str:
    base_values: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbols: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    index_tracker: int = 0
    accumulated_result: List[str] = []

    def attach_symbols(times_remaining: int) -> None:
        if times_remaining == 0:
            return
        accumulated_result.append(roman_symbols[index_tracker])
        attach_symbols(times_remaining - 1)

    while True:
        if value <= 0:
            break
        counts: int = value // base_values[index_tracker]
        value %= base_values[index_tracker]
        attach_symbols(counts)
        index_tracker += 1
        if index_tracker >= len(base_values):
            break

    return "".join(accumulated_result).lower()