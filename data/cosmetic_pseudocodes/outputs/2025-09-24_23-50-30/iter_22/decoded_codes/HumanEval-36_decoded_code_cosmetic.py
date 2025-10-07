from typing import Set


def fizz_buzz(integer_n: int) -> int:
    captured_values: Set[int] = set()
    index_x: int = 0
    while index_x < integer_n:
        if (index_x % 11 == 0) or (index_x % 13 == 0):
            captured_values.add(index_x)
        index_x += 1

    merged_text: str = "".join(str(element_y) for element_y in captured_values)

    total_sevens: int = sum(1 for symbol_z in merged_text if symbol_z == '7')

    return total_sevens