from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for string_item in list_of_strings:
        tally = 0
        for symbol in string_item:
            # Check if integer value of symbol is odd
            if int(symbol) % 2 != 0:
                tally += 1
        message = (
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
    return output_collection