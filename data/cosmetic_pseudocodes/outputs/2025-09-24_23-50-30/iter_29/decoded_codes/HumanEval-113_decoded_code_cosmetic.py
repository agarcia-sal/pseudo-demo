from typing import List


def odd_count(input_strings: List[str]) -> List[str]:
    def process_element(idx: int) -> List[str]:
        if idx == len(input_strings):
            return []
        current_item = input_strings[idx]
        odd_digit_total = sum(1 for digit_char in current_item if int(digit_char) % 2 != 0)
        formed_message = (
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
        return [formed_message] + process_element(idx + 1)

    return process_element(0)