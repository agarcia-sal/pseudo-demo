from typing import List

def odd_count(lst: List[List[int]]) -> List[str]:
    res = []
    for arr in lst:
        n = sum(1 for d in arr if int(d) % 2 == 1)
        res.append(f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput.")
    return res