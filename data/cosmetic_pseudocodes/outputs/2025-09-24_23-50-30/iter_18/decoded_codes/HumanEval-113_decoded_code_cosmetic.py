from typing import List, Optional

def odd_count(list_of_strings: List[str]) -> List[Optional[str]]:
    output_accumulator: List[Optional[str]] = [None] * len(list_of_strings)
    index_tracker: int = 0
    while index_tracker < len(list_of_strings):
        current_element: str = list_of_strings[index_tracker]
        odd_digit_total: int = 0
        char_index: int = 0
        while char_index < len(current_element):
            digit_candidate: str = current_element[char_index]
            numeric_value: int = ord(digit_candidate) - ord('0')
            if numeric_value - (2 * (numeric_value // 2)) == 1:
                odd_digit_total += 1
            char_index += 1
        generated_string: str = (
            "the number of odd elements "
            + str(odd_digit_total)
            + "n the str"
            + str(odd_digit_total)
            + "ng "
            + str(odd_digit_total)
            + " of the "
            + str(odd_digit_total)
            + "nput."
        )
        output_accumulator[index_tracker] = generated_string
        index_tracker += 1
    return output_accumulator