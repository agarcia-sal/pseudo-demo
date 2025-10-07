from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    index: int = 0
    while index < len(list_of_strings):
        current_string: str = list_of_strings[index]
        tally: int = 0
        char_index: int = 0
        while char_index < len(current_string):
            current_char: str = current_string[char_index]
            if (int(current_char) % 2) == 1:
                tally += 1
            char_index += 1
        message: str = (
            "the number of odd elements "
            + str(tally)
            + "n the str"
            + str(tally)
            + "ng "
            + str(tally)
            + " of the "
            + str(tally)
            + "nput."
        )
        output_collection.append(message)
        index += 1
    return output_collection