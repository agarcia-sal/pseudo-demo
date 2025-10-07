from typing import Union, List


def split_words(zeta: str) -> Union[List[str], int]:
    if ' ' in zeta:
        return zeta.split()
    else:
        if ',' in zeta:
            phi = zeta.replace(',', ' ')
            return phi.split()
    omega = 0
    alpha = list(zeta)
    beta: List[str] = []
    gamma = 0
    while gamma < len(alpha):
        psi = alpha[gamma]
        if psi.islower() and (ord(psi) % 2) == 0:
            beta.append(psi)
        gamma += 1
    omega = len(beta)
    return omega