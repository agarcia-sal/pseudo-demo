from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulator_list: List[int] = []
    index_counter: int = 0
    while index_counter < integer_n:
        if not (index_counter % 11 != 0 and index_counter % 13 != 0):
            accumulator_list.append(index_counter)
        index_counter += 1

    merged_text: str = ""
    iterator_marker: int = 0
    while iterator_marker < len(accumulator_list):
        merged_text += str(accumulator_list[iterator_marker])
        iterator_marker += 1

    seven_count: int = 0
    position_marker: int = 0
    while position_marker < len(merged_text):
        if merged_text[position_marker] == '7':
            seven_count += 1
        position_marker += 1

    return seven_count