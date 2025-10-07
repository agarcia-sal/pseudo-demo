from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    acc_result: List[str] = []

    def process_string(idx: int) -> List[str]:
        if idx == len(list_of_strings):
            return acc_result
        current_str = list_of_strings[idx]
        odd_digit_tally = sum(1 for ch in current_str if (int(ch) % 2) != 0)
        assembled_text = (
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
        acc_result.append(assembled_text)
        return process_string(idx + 1)

    return process_string(0)