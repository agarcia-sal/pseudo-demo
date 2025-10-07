from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_string: str = list_of_strings[idx]
        odd_counter: int = 0
        pos: int = 0
        while pos < len(current_string):
            digit_char: str = current_string[pos]
            if int(digit_char) % 2 == 1:
                odd_counter += 1
            pos += 1
        message: str = (
            "the number of odd elements "
            + str(odd_counter)
            + "n the str"
            + str(odd_counter)
            + "ng "
            + str(odd_counter)
            + " of the "
            + str(odd_counter)
            + "nput."
        )
        accumulator.append(message)
        idx += 1
    return accumulator