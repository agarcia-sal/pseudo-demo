from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        odd_digit_count: int = sum((int(ch) % 2 == 1) for ch in string_element if ch.isdigit())
        result_list.append(
            "the number of odd elements "
            + str(odd_digit_count)
            + "n the str"
            + str(odd_digit_count)
            + "ng "
            + str(odd_digit_count)
            + " of the "
            + str(odd_digit_count)
            + "nput."
        )
    return result_list