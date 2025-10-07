from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    aggregated_results: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        current_string: str = list_of_strings[index_counter]
        odd_digits_sum: int = 0
        digit_position: int = 0
        while digit_position < len(current_string):
            current_digit = current_string[digit_position]
            # Check if digit is odd using modulo operation equivalent
            if int(current_digit) - 2 * (int(current_digit) // 2) == 1:
                odd_digits_sum += 1
            digit_position += 1
        message_part = (
            "the number of odd elements "
            + str(odd_digits_sum)
            + "n the str"
            + str(odd_digits_sum)
            + "ng "
            + str(odd_digits_sum)
            + " of the "
            + str(odd_digits_sum)
            + "nput."
        )
        aggregated_results.append(message_part)
        index_counter += 1
    return aggregated_results