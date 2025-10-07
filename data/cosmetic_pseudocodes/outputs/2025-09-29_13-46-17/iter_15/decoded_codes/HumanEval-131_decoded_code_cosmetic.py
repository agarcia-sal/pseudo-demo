from typing import Union


def digits(n: Union[int, str]) -> int:
    def inner(xi: int, psi: int, zeta: str) -> int:
        if zeta == "":
            return xi if psi != 0 else 0
        omega = ord(zeta[0]) - ord('0')  # ASCII_TO_INT of first char
        theta = zeta[1:]  # remainder string
        if omega % 2 != 0:  # omega is odd
            return inner(xi * omega, psi + 1, theta)
        else:
            return inner(xi, psi, theta)

    return inner(1, 0, str(n))