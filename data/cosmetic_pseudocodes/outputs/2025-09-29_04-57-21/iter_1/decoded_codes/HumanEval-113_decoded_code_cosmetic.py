from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    for element_string in list_of_strings:
        odd_digit_total: int = 0
        for char_digit in element_string:
            if int(char_digit) % 2 == 1:
                odd_digit_total += 1
        message = (
            "the number of odd elements "
            + str(odd_digit_total)
            + "n the str"
            + str(odd_digit_total)
            + "ng "
            + str(odd_digit_total)
            + " of the "
            + str(odd_digit_total)
            + "nput."
        )
        output_collection.append(message)
    return output_collection