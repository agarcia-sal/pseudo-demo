from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result: List[str] = []
    for string_element in list_of_strings:
        count_odd_digits = sum(1 for digit in string_element if digit.isdigit() and int(digit) % 2 == 1)
        formatted_string = (
            "the number of odd elements "
            + str(count_odd_digits)
            + "n the str"
            + str(count_odd_digits)
            + "ng "
            + str(count_odd_digits)
            + " of the "
            + str(count_odd_digits)
            + "nput."
        )
        result.append(formatted_string)
    return result