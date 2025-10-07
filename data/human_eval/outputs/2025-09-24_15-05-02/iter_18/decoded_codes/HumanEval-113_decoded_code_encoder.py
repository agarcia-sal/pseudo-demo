from typing import List

def odd_count(lst: List[List[int]]) -> List[str]:
    res: List[str] = []
    for arr in lst:
        n: int = sum(1 for d in arr if d % 2 == 1)
        res.append(
            "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        )
    return res