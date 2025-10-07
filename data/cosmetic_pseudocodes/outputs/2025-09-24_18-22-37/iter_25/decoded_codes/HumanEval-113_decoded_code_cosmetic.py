from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(list_of_strings):
        current_string: str = list_of_strings[index_tracker]
        odd_digit_counter: int = 0
        char_index: int = 0
        while char_index < len(current_string):
            digit_char: str = current_string[char_index]
            digit_value: int = int(digit_char)
            if digit_value % 2 == 1:
                odd_digit_counter += 1
            char_index += 1

        prefix_text: str = "the number of odd elements "
        mid_text1: str = "n the str"
        mid_text2: str = "ng "
        mid_text3: str = " of the "
        suffix_text: str = "nput."
        count_text: str = str(odd_digit_counter)

        combined_message: str = (
            prefix_text
            + count_text
            + mid_text1
            + count_text
            + mid_text2
            + count_text
            + mid_text3
            + count_text
            + suffix_text
        )

        accumulator.append(combined_message)
        index_tracker += 1
    return accumulator