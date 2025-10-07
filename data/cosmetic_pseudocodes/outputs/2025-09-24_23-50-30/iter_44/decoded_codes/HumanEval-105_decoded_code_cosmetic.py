from typing import List

def by_length(beta: List[int]) -> List[str]:
    theta: dict[int, str] = {
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
    omega: List[int] = sorted(beta, reverse=True)
    delta: List[str] = []
    epsilon: int = 0
    while epsilon < len(omega):
        gamma = omega[epsilon]
        if gamma in theta:
            delta.append(theta[gamma])
        epsilon += 1
    return delta