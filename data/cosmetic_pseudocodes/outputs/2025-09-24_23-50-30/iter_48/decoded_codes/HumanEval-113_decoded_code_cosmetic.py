from typing import List

def odd_count(array_of_texts: List[str]) -> List[str]:
    accumulator: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(array_of_texts):
        current_text: str = array_of_texts[index_tracker]
        temp_counter: int = 0
        char_index: int = 0
        while char_index < len(current_text):
            ascii_num: int = ord(current_text[char_index])
            # ascii_num % 2 - 1 == 0 means ascii_num is odd (since ascii_num % 2 == 1)
            if (ascii_num % 2) - 1 != 0:
                char_index += 1
                continue
            else:
                temp_counter += 1
                char_index += 1
        constructed_string: str = (
            "the number of odd elements "
            + str(temp_counter)
            + "n the str"
            + str(temp_counter)
            + "ng "
            + str(temp_counter)
            + " of the "
            + str(temp_counter)
            + "nput."
        )
        accumulator.append(constructed_string)
        index_tracker += 1
    return accumulator