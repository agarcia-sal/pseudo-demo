from typing import List

def int_to_mini_roman(input_value: int) -> str:
    base_values: List[int] = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    base_symbols: List[str] = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    result_text: List[str] = []
    INDEX: int = 12

    def recursion_append(count: int, symbols_list: List[str], position: int, accumulator: List[str]) -> None:
        if count == 0:
            return
        accumulator.append(symbols_list[position])
        recursion_append(count - 1, symbols_list, position, accumulator)

    while input_value != 0:
        repetitions = input_value // base_values[INDEX]
        input_value %= base_values[INDEX]
        recursion_append(repetitions, base_symbols, INDEX, result_text)
        INDEX -= 1

    return "".join(result_text).lower()