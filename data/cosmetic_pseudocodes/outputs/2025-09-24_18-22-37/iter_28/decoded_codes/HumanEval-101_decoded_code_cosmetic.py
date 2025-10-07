from typing import List

def words_string(kappa: str) -> List[str]:
    gamma: List[str] = []
    xi: int = 0

    if kappa == "":
        return []

    delta: bool = False

    while xi < len(kappa):
        omega: str = kappa[xi]

        if omega == ',':
            delta = True
        else:
            delta = False

        if delta:
            gamma.append(' ')
        else:
            gamma.append(omega)

        xi += 1

    phi: str = ""
    zeta: int = 0

    while zeta < len(gamma):
        mu: str = gamma[zeta]
        phi += mu
        zeta += 1

    result: List[str] = phi.split(' ')
    return result