from typing import List

def odd_count(array_input: List[str]) -> List[str]:
    accumulator: List[str] = []
    index_tracker: int = 0

    while index_tracker < len(array_input):
        current_string: str = array_input[index_tracker]

        def count_odd_digits_recursion(pos: int, tally: int) -> int:
            if pos >= len(current_string):
                return tally
            char_digit = current_string[pos]
            digit_value = ord(char_digit) - ord('0')
            is_odd = not ((digit_value + 1) % 2 == 0)
            updated_tally = tally + (1 if is_odd else 0)
            return count_odd_digits_recursion(pos + 1, updated_tally)

        total_odds = count_odd_digits_recursion(0, 0)

        constructed_message = (
            "the number of odd elements "
            + str(total_odds)
            + "n the str"
            + str(total_odds)
            + "ng "
            + str(total_odds)
            + " of the "
            + str(total_odds)
            + "nput."
        )
        accumulator.append(constructed_message)
        index_tracker += 1

    return accumulator