from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_accumulator: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        current_str: str = list_of_strings[index_counter]
        odd_digits_tally: int = 0
        char_index: int = 0
        while char_index < len(current_str):
            current_char: str = current_str[char_index]
            digit_value: int = int(current_char)
            if digit_value % 2 == 1:
                odd_digits_tally += 1
            char_index += 1
        phrase_part1 = "the number of odd elements "
        phrase_part2 = "n the str"
        phrase_part3 = "ng "
        phrase_part4 = " of the "
        phrase_part5 = "nput."
        full_message = (
            phrase_part1
            + str(odd_digits_tally)
            + phrase_part2
            + str(odd_digits_tally)
            + phrase_part3
            + str(odd_digits_tally)
            + phrase_part4
            + str(odd_digits_tally)
            + phrase_part5
        )
        output_accumulator.append(full_message)
        index_counter += 1
    return output_accumulator