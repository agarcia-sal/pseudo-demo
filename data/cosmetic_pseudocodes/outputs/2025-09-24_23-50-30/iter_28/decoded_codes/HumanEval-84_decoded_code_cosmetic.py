from typing import Callable

def solve(beta: int) -> str:
    zeta: int = 0

    def recur(alpha: int, omega: str) -> int:
        nonlocal zeta
        if alpha == len(omega):
            return zeta
        lambd: str = omega[alpha]
        zeta += int(lambd)
        return recur(alpha + 1, omega)

    recur(0, str(beta))

    # Convert zeta to binary string with '0b' prefix, then remove first two and last character
    bstr: str = bin(zeta)
    if len(bstr) <= 3:  # If length is 3 or less, slicing results in empty string
        psi: str = ''
    else:
        psi = bstr[2:-1]

    return psi