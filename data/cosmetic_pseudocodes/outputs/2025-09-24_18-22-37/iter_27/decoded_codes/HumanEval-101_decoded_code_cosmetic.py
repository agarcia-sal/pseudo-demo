from typing import List

def words_string(zeta: str) -> List[str]:
    alpha: List[str] = []
    if zeta:
        iota: int = 0
        while iota < len(zeta):
            omega: str = zeta[iota]
            if omega == ',':
                alpha.append(' ')
            else:
                alpha.append(omega)
            iota += 1

        psi: str = ''
        mu: int = 0
        while mu < len(alpha):
            psi += alpha[mu]
            mu += 1

        delta: List[str] = psi.split()
        return delta

    return []