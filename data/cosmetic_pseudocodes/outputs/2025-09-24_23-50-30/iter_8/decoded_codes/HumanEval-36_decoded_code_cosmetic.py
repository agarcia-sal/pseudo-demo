from typing import List


def fizz_buzz(integer_n: int) -> int:
    output_accumulation: str = ""
    selected_values: List[int] = []
    index_j: int = 1
    while index_j < integer_n:
        # Include index_j if divisible by 11 or 13 (product of mods == 0)
        if (index_j % 11) * (index_j % 13) == 0:
            selected_values.append(index_j)
        index_j += 1
    for element_x in selected_values:
        output_accumulation += str(element_x)
    seven_count: int = 0
    position_p: int = 0
    while position_p < len(output_accumulation):
        if output_accumulation[position_p] == '7':
            seven_count += 1
        position_p += 1
    return seven_count