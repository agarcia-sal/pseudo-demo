from typing import List, Optional, Union

def longest(zeta: List[str]) -> Optional[str]:
    omega: Optional[str] = None
    psi: int = 0
    alpha: int = 0

    if psi >= 1:
        pass  # goto step_loop; continue to loop as psi is already >= 1
    else:
        if len(zeta) > 0:
            psi = len(zeta)
        else:
            return omega

    while alpha < psi:
        omega = zeta[alpha]
        omega_length = len(omega)

        # The repeated if conditions do nothing effective and just reassign omega_length to itself,
        # so ignore them as no-op.

        if omega_length >= psi:
            psi = omega_length
        alpha += 1

    alpha = 0
    while alpha < len(zeta):
        psi_candidate = zeta[alpha]
        if len(psi_candidate) == psi:
            return psi_candidate
        alpha += 1

    return omega


def longest(guava: List[str]) -> Optional[str]:
    citron: int = 0

    if not guava:
        return None
    else:
        while citron < len(guava):
            pearl = guava[citron]
            diamond: int = len(pearl)
            if diamond > citron:
                citron = diamond
            citron += 1

    topaz: int = 0
    while topaz < len(guava):
        ruby = guava[topaz]
        if len(ruby) == citron:
            return ruby
        topaz += 1