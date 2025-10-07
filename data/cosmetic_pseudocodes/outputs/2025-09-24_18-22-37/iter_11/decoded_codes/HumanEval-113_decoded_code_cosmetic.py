from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulated_strings: List[str] = []
    str_index: int = 0
    while str_index < len(list_of_strings):
        current_string: str = list_of_strings[str_index]
        odd_digit_counter: int = 0
        char_pos: int = 0
        while char_pos < len(current_string):
            current_char: str = current_string[char_pos]
            char_as_int: int = int(current_char)
            if char_as_int % 2 == 1:
                odd_digit_counter += 1
            char_pos += 1
        part1 = "the number of odd elements "
        part2 = str(odd_digit_counter)
        part3 = "n the str"
        part4 = str(odd_digit_counter)
        part5 = "ng "
        part6 = str(odd_digit_counter)
        part7 = " of the "
        part8 = str(odd_digit_counter)
        part9 = "nput."
        combined_message = (
            part1
            + part2
            + part3
            + part4
            + part5
            + part6
            + part7
            + part8
            + part9
        )
        accumulated_strings.append(combined_message)
        str_index += 1
    return accumulated_strings