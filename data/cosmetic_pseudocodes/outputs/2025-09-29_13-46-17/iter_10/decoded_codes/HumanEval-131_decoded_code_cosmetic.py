from typing import Callable


def digits(n: int) -> int:
    def ζ(xi: str, P: int, θ: int) -> int:
        if θ < 0 or xi == "":
            if P == 1 and θ == 0:
                return 0
            else:
                return P
        else:
            phi = ord(xi[0]) - ord('0')
            if (phi % 2) == 0:
                return ζ(xi[1:], P * phi, θ + 1)
            else:
                return ζ(xi[1:], P, θ)

    return ζ(str(n), 1, 0)