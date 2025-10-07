from typing import List

def odd_count(lst: List[List[str]]) -> List[str]:
    res: List[str] = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        text = f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput."
        res.append(text)
    return res