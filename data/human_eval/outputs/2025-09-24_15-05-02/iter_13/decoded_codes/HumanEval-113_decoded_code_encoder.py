from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result = []
    for string_element in list_of_strings:
        n = sum((int(digit) % 2 == 1) for digit in string_element)
        result.append(
            "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        )
    return result