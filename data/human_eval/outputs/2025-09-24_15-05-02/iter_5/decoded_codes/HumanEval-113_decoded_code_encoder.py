from typing import List

def odd_count(lst: List[str]) -> List[str]:
    result = []
    for arr in lst:
        odd_count = sum(1 for d in arr if int(d) % 2 == 1)
        message = (
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
        result.append(message)
    return result