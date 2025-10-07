from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:

    def count_odds(seq: str, pos: int, tally: int) -> int:
        if pos == len(seq):
            return tally
        digit_value = int(seq[pos])
        return count_odds(seq, pos + 1, tally + (digit_value & 1))

    accumulated_results: List[str] = []
    index = 0

    while index < len(list_of_strings):
        current_string = list_of_strings[index]
        odd_digit_total = count_odds(current_string, 0, 0)
        composed_message = (
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
        accumulated_results.append(composed_message)
        index += 1

    return accumulated_results