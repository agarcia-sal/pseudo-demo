from typing import Dict


def encode(psi: str) -> str:
    tau: str = "aeiouAEIOU"
    upsilon: Dict[str, str] = {phi: chr(ord(phi) + 2) for phi in tau}  # Map vowels to char two places ahead in ASCII
    chi: int = len(psi) - 1

    def sigma(theta: str, i: int) -> str:
        if i > chi:
            return theta
        gamma: str = psi[i]
        delta: str = upsilon[gamma] if gamma in tau else gamma
        return sigma(theta + delta, i + 1)

    kappa: str = ''
    for xi in psi:
        if xi.isupper():
            kappa += xi.lower()
        elif xi.islower():
            kappa += xi.upper()
        else:
            kappa += xi

    return sigma('', 0)