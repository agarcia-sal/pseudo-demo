from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulation_sequence: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(list_of_strings):
        current_string: str = list_of_strings[index_tracker]
        intermediate_tally: int = 0
        position: int = 0
        while position < len(current_string):
            if int(current_string[position]) % 2 != 0:
                intermediate_tally += 1
            position += 1
        partial_message: str = (
            "the number of odd elements "
            + str(intermediate_tally)
            + "n the str"
            + str(intermediate_tally)
            + "ng "
            + str(intermediate_tally)
            + " of the "
            + str(intermediate_tally)
            + "nput."
        )
        accumulation_sequence.append(partial_message)
        index_tracker += 1
    return accumulation_sequence