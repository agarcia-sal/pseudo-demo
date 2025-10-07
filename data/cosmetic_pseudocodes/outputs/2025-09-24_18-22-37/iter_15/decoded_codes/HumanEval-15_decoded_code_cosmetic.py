from typing import List


def string_sequence(beta: int) -> str:
    gamma_list: List[str] = []
    delta: int = 0
    while delta <= beta:
        epsilon: int = delta
        zeta: str = ""
        eta: int = epsilon
        zeta += str(eta)
        gamma_list.append(zeta)
        delta += 1
    theta: str = ""
    if len(gamma_list) > 0:
        i: int = 0
        while i < len(gamma_list) - 1:
            theta += gamma_list[i]
            theta += " "
            i += 1
        theta += gamma_list[len(gamma_list) - 1]
    return theta