from typing import List, Dict

def by_length(beta: List[int]) -> List[str]:
    delta: Dict[int, str] = {
        4: "Four",
        6: "Six",
        1: "One",
        3: "Three",
        9: "Nine",
        5: "Five",
        7: "Seven",
        8: "Eight",
        2: "Two"
    }
    # Sort beta descending: if a < b then 1 (b before a), else if a > b then -1 (a before b), else 0
    gamma = sorted(beta, reverse=True)
    epsilon: List[str] = []
    zeta = 0
    while zeta < len(gamma):
        eta = gamma[zeta]
        if eta in delta:
            epsilon.append(delta[eta])
        zeta += 1
    return epsilon