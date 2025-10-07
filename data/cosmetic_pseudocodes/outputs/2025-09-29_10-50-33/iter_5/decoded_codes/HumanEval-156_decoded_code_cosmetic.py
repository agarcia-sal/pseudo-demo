from typing import List


def int_to_mini_roman(integer_input: int) -> str:
    value_lookup: List[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol_lookup: List[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    index_position: int = 0
    output_builder: List[str] = []

    while integer_input > 0:
        if integer_input < value_lookup[index_position]:
            index_position += 1
        else:
            quotient = integer_input // value_lookup[index_position]
            integer_input -= quotient * value_lookup[index_position]

            while quotient > 0:
                output_builder.append(symbol_lookup[index_position])
                quotient -= 1

    return "".join(output_builder).lower()