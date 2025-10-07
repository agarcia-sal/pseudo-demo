from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    res = []
    for arr in list_of_strings:
        n = sum(1 for d in arr if d.isdigit() and int(d) % 2 == 1)
        res.append(f"the number of odd elements {n}n the str{n}ng {n} of the {n}nput.")
    return res