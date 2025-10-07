from typing import List, Dict, Union

def by_length(q: List[int]) -> List[str]:
    w: Dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    e: List[int] = sorted(q)  # sorts in ascending order by default
    r: List[str] = []
    i: int = 0
    while i < len(e):
        t: int = e[i]
        if t in w:
            r.append(w[t])
        i += 1
    return r