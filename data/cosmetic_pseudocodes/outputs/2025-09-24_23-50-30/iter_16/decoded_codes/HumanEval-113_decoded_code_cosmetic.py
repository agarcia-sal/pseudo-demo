from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    index: int = 0
    while index < len(list_of_strings):
        current_string: str = list_of_strings[index]
        odd_sum: int = 0
        position: int = 0
        while position < len(current_string):
            digit_value: int = int(current_string[position])
            if digit_value % 2 != 0:
                odd_sum += 1
            position += 1
        message = (
            "the number of odd elements "
            + str(odd_sum)
            + "n the str"
            + str(odd_sum)
            + "ng "
            + str(odd_sum)
            + " of the "
            + str(odd_sum)
            + "nput."
        )
        accumulator.append(message)
        index += 1
    return accumulator