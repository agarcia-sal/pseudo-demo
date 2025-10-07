from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulation: List[str] = []
    for string_item in list_of_strings:
        odd_digit_total = sum((int(ch) % 2 == 1) for ch in string_item if ch.isdigit())
        output_string = (
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
        accumulation.append(output_string)
    return accumulation