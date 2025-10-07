from typing import Iterable, List

def unique_digits(values_collection: Iterable[int]) -> List[int]:
    accumulator_var: List[int] = []
    iterator_index = 0
    values_list = list(values_collection)  # support indexing and length efficiently
    while iterator_index < len(values_list):
        current_candidate = values_list[iterator_index]
        digit_chars = str(current_candidate)
        check_flag = True
        position_index = 0
        while position_index < len(digit_chars) and check_flag:
            examined_char = digit_chars[position_index]
            numeric_val = int(examined_char)
            if numeric_val % 2 == 0:
                check_flag = False
            position_index += 1
        if check_flag:
            accumulator_var.append(current_candidate)
        iterator_index += 1
    result_sequence = accumulator_var
    result_sequence.sort()
    return result_sequence