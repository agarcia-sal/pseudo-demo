from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        odd_count: int = sum(1 for digit in string_element if digit.isdigit() and int(digit) % 2 == 1)
        formatted_string: str = (
            "the number of odd elements "
            + str(odd_count)
            + "n the str"
            + str(odd_count)
            + "ng "
            + str(odd_count)
            + " of the "
            + str(odd_count)
            + "nput."
        )
        result_list.append(formatted_string)
    return result_list