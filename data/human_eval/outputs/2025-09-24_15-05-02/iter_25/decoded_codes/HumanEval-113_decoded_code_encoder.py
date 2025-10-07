from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result: List[str] = []
    for string_element in list_of_strings:
        count_odd_digits = sum((int(char) % 2 == 1) for char in string_element if char.isdigit())
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