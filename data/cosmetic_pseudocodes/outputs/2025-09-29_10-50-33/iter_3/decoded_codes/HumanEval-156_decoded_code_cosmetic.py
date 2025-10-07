from typing import List

def int_to_mini_roman(input_value: int) -> str:
    numerals_arr: List[int] = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols_arr: List[str] = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    index_var: int = 12
    output_accumulator: List[str] = []

    def append_repetitions(times: int, symbol_index: int) -> None:
        if times == 0:
            return
        output_accumulator.extend([symbols_arr[symbol_index]] * times)

    while input_value != 0:
        quotient_part = input_value // numerals_arr[index_var]
        input_value = input_value % numerals_arr[index_var]

        append_repetitions(quotient_part, index_var)

        index_var -= 1

    return "".join(output_accumulator).lower()