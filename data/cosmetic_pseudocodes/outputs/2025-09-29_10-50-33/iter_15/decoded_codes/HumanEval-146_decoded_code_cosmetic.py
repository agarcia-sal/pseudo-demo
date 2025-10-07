from typing import Sequence

def specialFilter(sequence_of_values: Sequence[int]) -> int:
    count_accumulator: int = 0
    index_pointer: int = 0
    odd_collection = {1, 3, 5, 7, 9}  # use a set for O(1) membership tests

    while index_pointer < len(sequence_of_values):
        current_element = sequence_of_values[index_pointer]

        if current_element > 10:
            textual_form = str(current_element)

            first_digit_numeric = int(textual_form[0])
            last_digit_numeric = int(textual_form[-1])

            condition_one = first_digit_numeric in odd_collection
            condition_two = last_digit_numeric in odd_collection

            if condition_one and condition_two:
                count_accumulator += 1

        index_pointer += 1

    return count_accumulator