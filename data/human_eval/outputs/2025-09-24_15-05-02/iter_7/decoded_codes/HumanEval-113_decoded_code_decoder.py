from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list = []
    for string_element in list_of_strings:
        odd_count = sum(1 for ch in string_element if ch.isdigit() and int(ch) % 2 == 1)
        formatted_string = (
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