from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    aggregated_results: List[str] = []
    process_index: int = 0

    while process_index < len(list_of_strings):
        current_string: str = list_of_strings[process_index]
        accumulator: int = 0
        char_pos: int = 0

        while char_pos < len(current_string):
            if (int(current_string[char_pos]) & 1) == 1:
                accumulator += 1
            char_pos += 1

        aggregated_results.append(
            "the number of odd elements "
            + str(accumulator)
            + "n the str"
            + str(accumulator)
            + "ng "
            + str(accumulator)
            + " of the "
            + str(accumulator)
            + "nput."
        )
        process_index += 1

    return aggregated_results