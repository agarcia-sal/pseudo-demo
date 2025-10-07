from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    output: List[str] = []
    for element in list_of_strings:
        odd_count_tracker = 0
        for char in element:
            # Count if character is an odd digit
            if char.isdigit() and int(char) % 2 == 1:
                odd_count_tracker += 1
        message = (
            "the number of odd elements "
            + str(odd_count_tracker)
            + "n the str"
            + str(odd_count_tracker)
            + "ng "
            + str(odd_count_tracker)
            + " of the "
            + str(odd_count_tracker)
            + "nput."
        )
        output.append(message)
    return output