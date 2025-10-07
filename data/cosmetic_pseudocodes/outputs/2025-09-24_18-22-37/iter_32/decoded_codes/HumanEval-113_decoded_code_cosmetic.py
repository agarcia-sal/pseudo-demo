from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(list_of_strings):
        current_string: str = list_of_strings[index_tracker]
        temp_counter: int = 0
        char_index: int = 0
        while char_index < len(current_string):
            current_char: str = current_string[char_index]
            numeric_value: int = int(current_char)
            if numeric_value % 2 == 1:
                temp_counter += 1
            char_index += 1
        formatted_text: str = (
            "the number of odd elements " + str(temp_counter) +
            "n the str" + str(temp_counter) +
            "ng " + str(temp_counter) +
            " of the " + str(temp_counter) + "nput."
        )
        output_collection.append(formatted_text)
        index_tracker += 1
    return output_collection