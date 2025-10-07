from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        # Count digits that are odd
        odd_count = sum((int(ch) % 2 == 1) for ch in string_element if ch.isdigit())
        # Construct the formatted string as per the pseudocode
        formatted_string = (
            "the number of odd elements " + str(odd_count) +
            "n the str" + str(odd_count) +
            "ng " + str(odd_count) +
            " of the " + str(odd_count) +
            "nput."
        )
        result_list.append(formatted_string)
    return result_list