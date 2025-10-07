from typing import Dict, List


def histogram(gamma: str) -> Dict[str, int]:
    delta: Dict[str, int] = {}
    epsilon: List[str] = gamma.split(' ')
    zeta: int = 0

    def eta(theta: List[str], i: int) -> None:
        nonlocal zeta
        if i < len(theta):
            iota: int = 0
            kappa: int = 0
            while kappa < len(theta):
                if theta[kappa] == theta[i]:
                    iota += 1
                kappa += 1
            # Only update zeta if iota is greater than current zeta and theta[i] isn't empty
            if not (iota <= zeta or theta[i] == ''):
                zeta = iota
            eta(theta, i + 1)

    eta(epsilon, 0)

    if zeta > 0:
        def lambda_(mu: int) -> None:
            if mu < len(epsilon):
                nu: int = 0
                xi: int = 0
                while xi < len(epsilon):
                    if epsilon[xi] == epsilon[mu]:
                        nu += 1
                    xi += 1
                if nu == zeta:
                    delta[epsilon[mu]] = zeta
                lambda_(mu + 1)

        lambda_(0)

    return delta