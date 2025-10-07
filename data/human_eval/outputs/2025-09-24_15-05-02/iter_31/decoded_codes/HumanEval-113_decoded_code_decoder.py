from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        count_of_odd_digits = sum(int(d) % 2 == 1 for d in string_element if d.isdigit())
        s = (
            "the number of odd elements "
            + str(count_of_odd_digits)
            + "n the str"
            + str(count_of_odd_digits)
            + "ng "
            + str(count_of_odd_digits)
            + " of the "
            + str(count_of_odd_digits)
            + "nput."
        )
        result_list.append(s)
    return result_list