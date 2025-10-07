from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    iterator_outer: int = 0
    while iterator_outer < len(list_of_strings):
        current_str: str = list_of_strings[iterator_outer]
        odd_digit_counter: int = 0
        position_inner: int = 0
        while position_inner < len(current_str):
            digit_char: str = current_str[position_inner]
            if (ord(digit_char) - ord('0')) % 2 != 0:
                odd_digit_counter += 1
            position_inner += 1
        assembled_message = (
            "the number of odd elements "
            + str(odd_digit_counter)
            + "n the str"
            + str(odd_digit_counter)
            + "ng "
            + str(odd_digit_counter)
            + " of the "
            + str(odd_digit_counter)
            + "nput."
        )
        output_collection.append(assembled_message)
        iterator_outer += 1
    return output_collection