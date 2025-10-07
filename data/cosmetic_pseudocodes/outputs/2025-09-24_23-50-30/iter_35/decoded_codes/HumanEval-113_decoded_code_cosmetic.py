from typing import List

def odd_count(sequence_of_texts: List[str]) -> List[str]:
    accumulation: List[str] = []
    index_var: int = 0

    while index_var < len(sequence_of_texts):
        def inner_func(pos: int, acc: int) -> int:
            if pos == len(sequence_of_texts[index_var]):
                return acc
            current_char = sequence_of_texts[index_var][pos]
            acc += 1 if (ord(current_char) - ord('0')) % 2 != 0 else 0
            return inner_func(pos + 1, acc)

        odd_digit_tally = inner_func(0, 0)
        prefix = "the number of odd elements "
        middle1 = "n the str"
        middle2 = "ng "
        middle3 = " of the "
        suffix = "nput."
        joined_string = (
            prefix
            + str(odd_digit_tally)
            + middle1
            + str(odd_digit_tally)
            + middle2
            + str(odd_digit_tally)
            + middle3
            + str(odd_digit_tally)
            + suffix
        )
        accumulation.append(joined_string)
        index_var += 1

    return accumulation