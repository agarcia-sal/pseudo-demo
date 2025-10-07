from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result_list: List[str] = []
    index_outer: int = 0
    while index_outer < len(list_of_strings):
        current_string: str = list_of_strings[index_outer]
        odd_digit_count: int = 0
        index_inner: int = 0
        while index_inner < len(current_string):
            char_val: str = current_string[index_inner]
            if not (int(char_val) % 2 == 0):
                odd_digit_count += 1
            index_inner += 1
        formatted_message: str = (
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
        result_list.append(formatted_message)
        index_outer += 1
    return result_list