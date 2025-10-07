from typing import List, Dict

def by_length(alpha: List[int]) -> List[str]:
    beta: Dict[int, str] = {
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
    gamma: List[int] = sorted(alpha, reverse=True)
    delta: List[str] = []

    def recur(epsilon: List[int]) -> None:
        if not epsilon:
            return
        zeta = epsilon[0]
        if zeta in beta:
            delta.append(beta[zeta])
        recur(epsilon[1:])

    recur(gamma)
    return delta