from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_str: str = list_of_strings[idx]
        odd_digit_count: int = 0

        pos: int = 0
        while pos < len(current_str):
            digit_char: str = current_str[pos]
            if digit_char.isdigit() and int(digit_char) % 2 == 1:
                odd_digit_count += 1
            pos += 1

        constructed_message: str = (
            "the number of odd elements " + str(odd_digit_count)
            + "n the str" + str(odd_digit_count)
            + "ng " + str(odd_digit_count)
            + " of the " + str(odd_digit_count)
            + "nput."
        )

        output_collection.append(constructed_message)
        idx += 1

    return output_collection