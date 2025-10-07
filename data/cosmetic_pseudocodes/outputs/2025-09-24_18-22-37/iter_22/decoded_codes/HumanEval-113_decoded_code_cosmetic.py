from typing import List


def odd_count(input_strings: List[str]) -> List[str]:
    collected_results: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(input_strings):
        current_sequence: str = input_strings[index_tracker]
        iter_position: int = 0
        odd_digit_tally: int = 0
        while True:
            if iter_position >= len(current_sequence):
                break
            current_char: str = current_sequence[iter_position]
            numerical_value: int = int(current_char)
            if numerical_value % 2 == 1:
                odd_digit_tally += 1
            iter_position += 1

        prefix_part: str = "the number of odd elements "
        middle_part: str = "n the str"
        mid_number: str = str(odd_digit_tally)
        suffix_part_a: str = "ng "
        suffix_part_b: str = " of the "
        suffix_part_c: str = "nput."

        composed_message: str = (
            prefix_part
            + mid_number
            + middle_part
            + mid_number
            + suffix_part_a
            + mid_number
            + suffix_part_b
            + mid_number
            + suffix_part_c
        )
        collected_results.append(composed_message)
        index_tracker += 1
    return collected_results