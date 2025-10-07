from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    def helper(index_accumulator: int, result_accumulator: List[str]) -> List[str]:
        if index_accumulator >= len(list_of_strings):
            return result_accumulator
        current_string = list_of_strings[index_accumulator]
        iterator = 0
        tally = 0
        while iterator < len(current_string):
            digit_char = current_string[iterator]
            if int(digit_char) % 2 == 1:
                tally += 1
            iterator += 1
        composed_message = (
            "the number of odd elements "
            + str(tally)
            + "n the str"
            + str(tally)
            + "ng "
            + str(tally)
            + " of the "
            + str(tally)
            + "nput."
        )
        return helper(index_accumulator + 1, result_accumulator + [composed_message])

    return helper(0, [])