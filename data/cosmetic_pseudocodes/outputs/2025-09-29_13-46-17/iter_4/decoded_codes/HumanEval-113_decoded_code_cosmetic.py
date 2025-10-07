from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []

    def helper(index: int) -> List[str]:
        if index == len(list_of_strings):
            return accumulator
        current_string: str = list_of_strings[index]
        odd_digit_tally: int = 0
        char_index: int = 0
        while char_index < len(current_string):
            candidate_char = current_string[char_index]
            # Check if character represents an odd digit
            if (int(candidate_char) - 1) % 2 == 0:
                odd_digit_tally += 1
            char_index += 1
        composed_message = (
            "the number of odd elements "
            + str(odd_digit_tally)
            + "n the str"
            + str(odd_digit_tally)
            + "ng "
            + str(odd_digit_tally)
            + " of the "
            + str(odd_digit_tally)
            + "nput."
        )
        accumulator.append(composed_message)
        return helper(index + 1)

    return helper(0)