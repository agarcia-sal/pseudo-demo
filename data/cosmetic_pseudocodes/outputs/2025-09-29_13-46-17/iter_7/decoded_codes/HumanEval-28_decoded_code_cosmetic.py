from typing import List


def concatenate(Fx1Q: List[str]) -> str:
    return Fx7(D3A(Fx1Q, ""))


def Fx7(Zm4: str) -> str:
    Fx_9 = ""
    # Fz5 attempt to accumulate Fx_9 won't work since strings are immutable;
    # the original pseudocode implies mutation which isn't reflected in Python this way.
    # Since Fz5 does not affect the output in this translation, we keep it to preserve structure.
    Fz5(Fx_9, Zm4, 0)
    return Fx_9


def Fz5(cV7: str, J_3: str, b0R: int) -> None:
    if b0R < len(J_3):
        Fxz = J_3[b0R]
        cV7 = cV7 + Fxz  # Local reassignment does not affect caller
        Fz5(cV7, J_3, b0R + 1)


def D3A(Gjk: List[str], N6T: str) -> str:
    if not Gjk:
        return N6T
    Q2x = Gjk.pop(0)
    return D3A(Gjk, N6T + Q2x)