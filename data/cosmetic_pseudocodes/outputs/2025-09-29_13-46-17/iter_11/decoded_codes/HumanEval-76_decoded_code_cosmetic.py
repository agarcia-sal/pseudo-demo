from typing import Callable

def is_simple_power(i: int, q: int) -> bool:
    def xi(z: int, c: int) -> bool:
        if c == 1:
            return z == 1
        else:
            return psi(1, c, z)

    def psi(w: int, t: int, f: int) -> bool:
        if w < f:
            return psi(w * t, t, f)
        else:
            return w == f

    return xi(i, q)