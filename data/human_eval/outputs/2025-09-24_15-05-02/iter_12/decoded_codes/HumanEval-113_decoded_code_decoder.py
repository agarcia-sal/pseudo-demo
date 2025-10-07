from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        count_odd_digits = sum(1 for d in string_element if d.isdigit() and int(d) % 2 == 1)
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
        result_list.append(formatted_string)
    return result_list