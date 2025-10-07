from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for idx in range(len(list_of_strings)):
        current_entry = list_of_strings[idx]
        tally_odd_digits = sum(1 for char_value in current_entry if char_value.isdigit() and int(char_value) % 2 != 0)
        assembled_text = (
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
        output_collection.append(assembled_text)
    return output_collection