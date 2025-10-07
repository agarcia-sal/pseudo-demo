from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_string: str = list_of_strings[idx]
        odd_digit_counter: int = 0
        char_index: int = 0
        while char_index < len(current_string):
            digit_char: str = current_string[char_index]
            if int(digit_char) % 2 != 0:
                odd_digit_counter += 1
            char_index += 1
        output_text = "the number of odd elements "
        output_text += str(odd_digit_counter) + "n the str"
        output_text += str(odd_digit_counter) + "ng "
        output_text += str(odd_digit_counter) + " of the "
        output_text += str(odd_digit_counter) + "nput."
        output_collection.append(output_text)
        idx += 1
    return output_collection