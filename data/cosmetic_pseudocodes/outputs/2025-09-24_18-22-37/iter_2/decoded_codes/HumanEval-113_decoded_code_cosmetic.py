from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for string_item in list_of_strings:
        odd_digit_tally: int = 0
        for character in string_item:
            if character.isdigit() and int(character) % 2 == 1:
                odd_digit_tally += 1
        message = (
            "the number of odd elements "
            + str(odd_digit_tally)
            + "n the str"
            + str(odd_digit_tally)
            + "ng "
            + str(odd_digit_tally)
            + " of the "
            + str(odd_digit_tally)
            + "nput."
        )
        output_collection.append(message)
    return output_collection