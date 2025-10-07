from typing import List

def odd_count(lst: List[List[int]]) -> List[str]:
    res = []
    for arr in lst:
        n = sum(1 for d in arr if int(d) % 2 == 1)
        phrase = ("the number of odd elements " + str(n) + "n the str" + str(n) + "ng " +
                  str(n) + " of the " + str(n) + "nput.")
        res.append(phrase)
    return res