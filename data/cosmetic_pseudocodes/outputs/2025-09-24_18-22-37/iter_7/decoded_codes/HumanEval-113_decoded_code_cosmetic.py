from typing import List

def odd_count(sequence_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    index: int = 0
    while index < len(sequence_of_strings):
        current_string: str = sequence_of_strings[index]
        odd_digits_counter: int = 0
        char_index: int = 0
        while char_index < len(current_string):
            current_character: str = current_string[char_index]
            numeric_value: int = int(current_character)
            if numeric_value % 2 != 0:
                odd_digits_counter += 1
            char_index += 1
        constructed_message: str = (
            "the number of odd elements "
            + str(odd_digits_counter)
            + "n the str"
            + str(odd_digits_counter)
            + "ng "
            + str(odd_digits_counter)
            + " of the "
            + str(odd_digits_counter)
            + "nput."
        )
        output_collection.append(constructed_message)
        index += 1
    return output_collection