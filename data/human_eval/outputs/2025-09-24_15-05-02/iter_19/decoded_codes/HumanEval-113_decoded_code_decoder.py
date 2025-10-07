from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        odd_count_value: int = sum(1 for ch in string_element if ch.isdigit() and int(ch) % 2 == 1)
        result_list.append(
            "the number of odd elements " + str(odd_count_value) +
            "n the str" + str(odd_count_value) +
            "ng " + str(odd_count_value) +
            " of the " + str(odd_count_value) +
            "nput."
        )
    return result_list