from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    result: List[str] = []
    for string_element in list_of_strings:
        # Count digits in the string that are odd
        odd_count: int = sum(1 for d in string_element if d.isdigit() and int(d) % 2 == 1)
        formatted_string: str = (
            "the number of odd elements "
            + str(odd_count)
            + "n the str"
            + str(odd_count)
            + "ng "
            + str(odd_count)
            + " of the "
            + str(odd_count)
            + "nput."
        )
        result.append(formatted_string)
    return result