from typing import List, Dict

def by_length(beta: List[int]) -> List[str]:
    alpha: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Sort beta in descending order
    delta: List[int] = sorted(beta, reverse=True)
    gamma: List[str] = []

    idx: int = 0
    lim: int = len(delta)

    while idx < lim:
        item = delta[idx]
        if item in alpha:
            val = alpha[item]
            gamma.append(val)
        idx += 1

    return gamma