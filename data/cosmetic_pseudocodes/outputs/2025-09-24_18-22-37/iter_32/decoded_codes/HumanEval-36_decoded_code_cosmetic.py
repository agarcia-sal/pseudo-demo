from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulator_list: List[int] = []
    index_counter: int = 0
    while index_counter < integer_n:
        divisible_by_eleven: bool = (index_counter % 11 == 0)
        divisible_by_thirteen: bool = (index_counter % 13 == 0)
        if not (divisible_by_eleven is False and divisible_by_thirteen is False):
            accumulator_list.append(index_counter)
        index_counter += 1

    result_string: str = ""
    element_position: int = 0
    while element_position < len(accumulator_list):
        current_value: int = accumulator_list[element_position]
        result_string += str(current_value)
        element_position += 1

    seven_counter: int = 0
    char_index: int = 0
    while char_index < len(result_string):
        current_char: str = result_string[char_index]
        if current_char == '7':
            seven_counter += 1
        char_index += 1

    return seven_counter