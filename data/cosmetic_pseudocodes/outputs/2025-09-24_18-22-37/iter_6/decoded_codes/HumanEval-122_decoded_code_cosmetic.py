from typing import List


def add_elements(list_integers: List[int], limit_k: int) -> int:
    accumulator_total = 0
    index_counter = 0
    while index_counter < limit_k:
        current_number = list_integers[index_counter]
        text_form = str(current_number)
        length_of_text = len(text_form)
        if not (length_of_text > 2):
            accumulator_total += current_number
        index_counter += 1
    return accumulator_total