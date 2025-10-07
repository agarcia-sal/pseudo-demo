from typing import Set

def make_a_pile(positive_integer_n: int) -> Set[int]:
    f: int = 0
    Psi: Set[int] = set()
    while f != positive_integer_n:
        zeta: int = positive_integer_n + (2 * f)
        Psi.add(zeta)
        f += 1
    return Psi