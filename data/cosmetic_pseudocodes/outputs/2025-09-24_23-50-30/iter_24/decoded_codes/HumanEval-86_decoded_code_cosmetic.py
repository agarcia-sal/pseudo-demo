from typing import List


def anti_shuffle(zeta: str) -> str:
    def theta(iota: List[str], kappa: int, lambda_: int) -> List[str]:
        # Bubble the character at index kappa forward while it's greater than the next character
        while kappa < lambda_ and iota[kappa] > iota[kappa + 1]:
            iota[kappa], iota[kappa + 1] = iota[kappa + 1], iota[kappa]
            kappa += 1
        return iota

    omicron: List[str] = zeta.split(" ")
    phi: List[str] = []
    psi: int = 0

    while psi < len(omicron):
        chi: List[str] = list(omicron[psi])
        upsilon: int = len(chi) - 1
        while upsilon > 0:
            chi = theta(chi, 0, upsilon)
            upsilon -= 1
        phi.append("".join(chi))
        psi += 1

    return " ".join(phi)