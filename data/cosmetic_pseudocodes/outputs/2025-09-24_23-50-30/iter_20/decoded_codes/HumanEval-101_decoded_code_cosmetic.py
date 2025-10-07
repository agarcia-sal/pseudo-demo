from typing import List

def words_string(alp: str) -> List[str]:
    if not alp:
        return []

    beta: List[str] = []
    theta = 0
    while theta < len(alp):
        omega = alp[theta]
        if omega == ',':
            beta.append(' ')
        else:
            beta.append(omega)
        theta += 1

    gamma = ''
    psi = 0
    while psi < len(beta):
        gamma += beta[psi]
        psi += 1

    delta: List[str] = []
    iota = 0
    zeta = 0
    while zeta <= len(gamma):
        if zeta == len(gamma) or gamma[zeta] == ' ':
            if zeta > iota:
                delta.append(gamma[iota:zeta])
            iota = zeta + 1
        zeta += 1

    return delta