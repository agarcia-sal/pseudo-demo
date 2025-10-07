from typing import List

def odd_count(string_sequence: List[str]) -> List[str]:
    def helper(accumulator: List[str], index: int) -> List[str]:
        if index >= len(string_sequence):
            return accumulator
        current_string = string_sequence[index]
        digit_collection = list(current_string)
        temp_sum = 0
        for char_element in digit_collection:
            numeric_char = int(char_element)
            if numeric_char % 2 != 0:
                temp_sum += 1
        constructed_text = (
            "the number of odd elements "
            + str(temp_sum)
            + "n the str"
            + str(temp_sum)
            + "ng "
            + str(temp_sum)
            + " of the "
            + str(temp_sum)
            + "nput."
        )
        return helper(accumulator + [constructed_text], index + 1)
    return helper([], 0)