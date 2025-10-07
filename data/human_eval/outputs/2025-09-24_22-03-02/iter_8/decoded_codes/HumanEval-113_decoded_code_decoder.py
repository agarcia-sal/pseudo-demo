from typing import List

def odd_count(lst: List[List[str]]) -> List[str]:
    res = []
    for arr in lst:
        n = 0
        for d in arr:
            if int(d) % 2 == 1:
                n += 1
        formatted_string = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(formatted_string)
    return res