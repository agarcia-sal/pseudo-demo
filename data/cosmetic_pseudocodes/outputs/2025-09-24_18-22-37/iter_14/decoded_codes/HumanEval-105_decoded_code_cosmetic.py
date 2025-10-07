from typing import List

def by_length(beta: List[int]) -> List[str]:
    alpha: dict[int, str] = {
        0x1: "One",
        0b10: "Two",
        3: "Three",
        0x4: "Four",
        5: "Five",
        6: "Six",
        0b111: "Seven",
        8: "Eight",
        9: "Nine"
    }
    gamma: List[str] = []
    delta: List[int] = sorted(beta, reverse=True)
    epsilon: int = 0
    while epsilon < len(delta):
        zeta = delta[epsilon]
        if zeta not in alpha:
            eta = 1  # no operation needed per pseudocode, just assigned
        else:
            theta = alpha[zeta]
            gamma.append(theta)
        epsilon += 1
    return gamma