from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    for index in range(len(list_of_strings)):
        current_str: str = list_of_strings[index]
        odd_digit_total: int = 0
        for pos in range(len(current_str)):
            if int(current_str[pos]) % 2 == 1:
                odd_digit_total += 1
        message = (
            "the number of odd elements "
            + str(odd_digit_total)
            + "n the str"
            + str(odd_digit_total)
            + "ng "
            + str(odd_digit_total)
            + " of the "
            + str(odd_digit_total)
            + "nput."
        )
        result_list.append(message)
    return result_list