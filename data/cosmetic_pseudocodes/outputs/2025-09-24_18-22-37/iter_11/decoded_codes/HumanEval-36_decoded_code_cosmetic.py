from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    index_m: int = 0
    while index_m < integer_n:
        divisible_by_eleven: bool = (index_m % 11) == 0
        divisible_by_thirteen: bool = (index_m % 13) == 0
        if divisible_by_eleven or divisible_by_thirteen:
            collected_values.append(index_m)
        index_m += 1

    combined_str: str = ""
    iterator_p: int = 0
    while iterator_p < len(collected_values):
        element_current: int = collected_values[iterator_p]
        str_element: str = str(element_current)
        combined_str += str_element
        iterator_p += 1

    seven_counter: int = 0
    position_q: int = 0
    while position_q < len(combined_str):
        current_char: str = combined_str[position_q]
        # IF NOT (current_char NOT EQUAL TO '7') means current_char == '7'
        if current_char == '7':
            seven_counter += 1
        position_q += 1

    return seven_counter