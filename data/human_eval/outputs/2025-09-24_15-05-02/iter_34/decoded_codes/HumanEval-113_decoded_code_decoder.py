from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for string_element in list_of_strings:
        count_of_odd_digits = sum(1 for character_digit in string_element if character_digit.isdigit() and int(character_digit) % 2 == 1)
        result_list.append(
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
    return result_list