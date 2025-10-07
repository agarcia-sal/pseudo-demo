from typing import List

def odd_count(list_of_digit_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for digit_string in list_of_digit_strings:
        odd_digit_count = 0
        for character in digit_string:
            if character.isdigit() and int(character) % 2 == 1:
                odd_digit_count += 1
        formatted_string = (
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
        result_list.append(formatted_string)
    return result_list