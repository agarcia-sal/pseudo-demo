from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list = []
    for string_element in list_of_strings:
        count_odd_digits = sum((int(digit) % 2 == 1) for digit in string_element if digit.isdigit())
        formatted_string = (
            "the number of odd elements " + str(count_odd_digits) +
            "n the str" + str(count_odd_digits) +
            "ng " + str(count_odd_digits) +
            " of the " + str(count_odd_digits) +
            "nput."
        )
        result_list.append(formatted_string)
    return result_list