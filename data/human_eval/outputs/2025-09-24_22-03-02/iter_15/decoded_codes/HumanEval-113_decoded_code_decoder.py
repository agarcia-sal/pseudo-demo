from typing import List

def odd_count(lst: List[str]) -> List[str]:
    res: List[str] = []
    for arr in lst:
        n: int = 0
        for d in arr:
            if int(d) % 2 == 1:
                n += 1
        text: str = "the number of odd elements " + str(n) + "n the str" + str(n) + "ng " + str(n) + " of the " + str(n) + "nput."
        res.append(text)
    return res