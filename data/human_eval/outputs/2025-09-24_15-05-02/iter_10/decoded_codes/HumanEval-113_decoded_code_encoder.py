from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list = []
    for string_element in list_of_strings:
        odd_digit_count = 0
        for character_digit in string_element:
            if character_digit.isdigit() and int(character_digit) % 2 == 1:
                odd_digit_count += 1
        output_string = (
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
        result_list.append(output_string)
    return result_list