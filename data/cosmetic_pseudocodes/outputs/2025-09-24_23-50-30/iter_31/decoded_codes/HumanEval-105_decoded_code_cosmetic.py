from typing import List

def by_length(beta: List[int]) -> List[str]:
    gamma: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    epsilon: List[int] = sorted(beta, reverse=True)
    zeta: List[str] = []

    def iterate_eta(delta: List[int]) -> None:
        if not delta:
            return
        theta = delta[0]
        if theta in gamma:
            zeta.append(gamma[theta])
        iterate_eta(delta[1:])

    iterate_eta(epsilon)
    return zeta