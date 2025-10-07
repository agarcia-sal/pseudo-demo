from typing import List, Dict


def parse_music(kappa: str) -> List[int]:
    psi: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def unfold(delta: List[int], omega: List[str]) -> List[int]:
        if not omega:
            return delta
        zeta, *upsilon = omega
        if zeta != '':
            delta.insert(0, psi[zeta])  # prepend psi[zeta]
        return unfold(delta, upsilon)

    eta: List[str] = kappa.split(' ')
    lambda_: List[int] = list(reversed(unfold([], eta)))
    return lambda_