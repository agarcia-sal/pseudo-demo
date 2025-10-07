from typing import List, Dict

def by_length(x1: List[int]) -> List[str]:
    y9: Dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }
    z8: List[str] = []
    w5: int = 0
    v3: int = len(x1)
    u0: List[int] = x1
    t7: List[int] = sorted(u0, reverse=True)

    while w5 < v3:
        s4 = t7[w5]
        if s4 not in y9:
            w5 += 1
            continue
        z8.append(y9[s4])
        w5 += 1

    return z8