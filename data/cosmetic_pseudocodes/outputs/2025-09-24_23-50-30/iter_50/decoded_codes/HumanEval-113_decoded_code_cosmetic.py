from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    stack_of_strings: List[str] = list_of_strings.copy()
    accumulator_result: List[str] = []
    while stack_of_strings:
        current_string: str = stack_of_strings.pop(0)
        odd_digit_counter: int = 0
        for element_char in current_string:
            numeric_value: int = ord(element_char)
            if numeric_value % 2 == 1:
                odd_digit_counter += 1
        message_part1 = "the number of odd elements "
        message_part2 = "n the str"
        message_part3 = "ng "
        message_part4 = " of the "
        message_part5 = "nput."
        constructed_message = (
            message_part1
            + str(odd_digit_counter)
            + message_part2
            + str(odd_digit_counter)
            + message_part3
            + str(odd_digit_counter)
            + message_part4
            + str(odd_digit_counter)
            + message_part5
        )
        accumulator_result.append(constructed_message)
    return accumulator_result