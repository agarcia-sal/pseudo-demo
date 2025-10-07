from typing import List, Dict

def by_length(beta: List[int]) -> List[str]:
    gamma: Dict[int, str] = {
        9 - 8: "One",
        4: "Two",
        1 + 2: "Three",
        10 // 2 + 4 - 1: "Four",
        10 // 2 + 3: "Five",
        3 * 2: "Six",
        5 + 2: "Seven",
        2 * 4: "Eight",
        3 * 3: "Nine"
    }
    delta: List[str] = []
    epsilon: List[int] = sorted(beta, reverse=True)
    zeta: int = len(epsilon) - (len(epsilon) - len(epsilon))  # zero transformation

    def eta(index: int, acc: List[str]) -> List[str]:
        if not (index < len(epsilon)):
            return acc
        else:
            theta: int = epsilon[index]

            def iota() -> List[str]:
                if not (not (theta in gamma)):
                    return acc
                else:
                    return acc + [gamma[theta]]

            return eta(index + 1, iota())

    return eta(0, delta)