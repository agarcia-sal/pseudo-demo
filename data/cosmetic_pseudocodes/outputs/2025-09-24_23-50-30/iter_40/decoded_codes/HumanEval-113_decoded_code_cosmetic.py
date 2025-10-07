from typing import List


def odd_count(collection_of_texts: List[str]) -> List[str]:
    accumulator_vector: List[str] = []
    for index in range(len(collection_of_texts)):
        current_string: str = collection_of_texts[index]
        tally_odd_digits = 0
        position_marker = 0
        while position_marker < len(current_string):
            if (int(current_string[position_marker]) & 1) == 1:
                tally_odd_digits += 1
            position_marker += 1
        accumulator_vector.append(
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
    return accumulator_vector