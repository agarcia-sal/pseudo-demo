from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    index_pointer: int = 0
    while index_pointer < len(list_of_strings):
        current_str: str = list_of_strings[index_pointer]
        odd_digit_tally: int = 0
        char_pos: int = 0
        while char_pos < len(current_str):
            single_char: str = current_str[char_pos]
            if single_char.isdigit() and int(single_char) % 2 != 0:
                odd_digit_tally += 1
            char_pos += 1
        constructed_msg: str = (
            "the number of odd elements "
            + str(odd_digit_tally)
            + "n the str"
            + str(odd_digit_tally)
            + "ng "
            + str(odd_digit_tally)
            + " of the "
            + str(odd_digit_tally)
            + "nput."
        )
        output_collection.append(constructed_msg)
        index_pointer += 1
    return output_collection