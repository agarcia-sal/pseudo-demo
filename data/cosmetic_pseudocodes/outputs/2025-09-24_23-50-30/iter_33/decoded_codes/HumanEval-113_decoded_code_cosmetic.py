from typing import List

def odd_count(collection_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    for string_candidate in collection_of_strings:
        temp_counter: int = 0
        for character_item in string_candidate:
            numeric_version: int = int(character_item)
            if numeric_version % 2 == 1:
                temp_counter += 1
        message: str = (
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
        accumulator.append(message)
    return accumulator