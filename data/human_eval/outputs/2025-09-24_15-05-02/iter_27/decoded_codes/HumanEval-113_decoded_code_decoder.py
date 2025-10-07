from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        count_odds: int = sum((int(digit) % 2 == 1) for digit in string_element if digit.isdigit())
        result_list.append(
            f"the number of odd elements {count_odds}n the str{count_odds}ng {count_odds} of the {count_odds}nput."
        )
    return result_list