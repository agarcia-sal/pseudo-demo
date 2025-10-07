from typing import List, Dict

def by_length(beta: List[int]) -> List[str]:
    alpha: Dict[int, str] = {
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
    gamma: List[str] = []
    delta: List[int] = sorted(beta, reverse=True)
    i: int = 0
    while i < len(delta):
        if delta[i] not in alpha:
            i += 1
            continue
        gamma.append(alpha[delta[i]])
        i += 1
    return gamma