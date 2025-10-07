from typing import Callable

def get_closest_vowel(omega: str) -> str:
    if len(omega) < 3:
        return ""

    theta: list[str] = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]
    kappa: int = len(omega) - 2

    def zeta(chi: int) -> str:
        if chi < 1:
            return ""
        if omega[chi] in theta:
            if omega[chi - 1] not in theta and omega[chi + 1] not in theta:
                return omega[chi]
            else:
                return zeta(chi - 1)
        else:
            return zeta(chi - 1)

    return zeta(kappa)