from typing import List

def words_string(gamma: str) -> List[str]:
    if gamma == "":
        return []
    delta: List[str] = []
    epsilon: int = 0

    while epsilon < len(gamma):
        zeta: str = gamma[epsilon]

        if zeta == ",":
            delta.append(" ")
        else:
            delta.append(zeta)

        epsilon += 1

    eta: str = ""
    theta: int = 0

    while theta < len(delta):
        eta += delta[theta]
        theta += 1

    return eta.split(" ")