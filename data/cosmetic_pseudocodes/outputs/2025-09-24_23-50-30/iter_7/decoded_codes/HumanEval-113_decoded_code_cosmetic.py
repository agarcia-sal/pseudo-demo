from typing import List

def odd_count(string_collection: List[str]) -> List[str]:
    accumulation_container: List[str] = []
    index_tracker: int = 0

    while index_tracker < len(string_collection):
        current_item: str = string_collection[index_tracker]

        tally_odd_digits: int = 0
        position_marker: int = 0

        while position_marker < len(current_item):
            element_char: str = current_item[position_marker]
            # Check if digit corresponds to an odd number using (int(digit) - 1) % 2 == 0
            if (int(element_char) - 1) % 2 == 0:
                tally_odd_digits += 1
            position_marker += 1

        accumulation_container.append(
            "the number of odd elements "
            + str(tally_odd_digits)
            + "n the str"
            + str(tally_odd_digits)
            + "ng "
            + str(tally_odd_digits)
            + " of the "
            + str(tally_odd_digits)
            + "nput."
        )

        index_tracker += 1

    return accumulation_container