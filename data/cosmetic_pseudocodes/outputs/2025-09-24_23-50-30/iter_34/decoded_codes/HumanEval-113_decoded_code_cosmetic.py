from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    acc: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        curr_string: str = list_of_strings[idx]
        odds_sum: int = 0
        pos: int = 0
        while pos < len(curr_string):
            chr: str = curr_string[pos]
            if int(chr) % 2 == 1:
                odds_sum += 1
            pos += 1
        msg = (
            "the number of odd elements "
            + str(odds_sum)
            + "n the str"
            + str(odds_sum)
            + "ng "
            + str(odds_sum)
            + " of the "
            + str(odds_sum)
            + "nput."
        )
        acc.append(msg)
        idx += 1
    return acc