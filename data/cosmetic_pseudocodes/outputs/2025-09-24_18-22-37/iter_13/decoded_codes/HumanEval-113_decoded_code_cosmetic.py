from typing import List


def odd_count(input_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx_outer: int = 0
    while idx_outer < len(input_strings):
        current_str: str = input_strings[idx_outer]
        idx_char: int = 0
        odd_digit_total: int = 0
        while True:
            if idx_char >= len(current_str):
                break
            current_char: str = current_str[idx_char]
            numeric_val: int = int(current_char)
            if numeric_val % 2 == 1:
                odd_digit_total += 1
            idx_char += 1
        prefix_text = "the number of odd elements "
        middle_text = "n the str"
        suffix_text = "ng "
        ending_text = " of the "
        input_text = "nput."
        concatenated_message = (
            prefix_text
            + str(odd_digit_total)
            + middle_text
            + str(odd_digit_total)
            + suffix_text
            + str(odd_digit_total)
            + ending_text
            + str(odd_digit_total)
            + input_text
        )
        output_collection.append(concatenated_message)
        idx_outer += 1
    return output_collection