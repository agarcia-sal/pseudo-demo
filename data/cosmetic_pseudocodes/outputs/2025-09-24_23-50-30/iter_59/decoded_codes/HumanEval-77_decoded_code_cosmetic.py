from math import exp, log

def iscube(A: float) -> bool:
    E: float = abs(A)

    def E_func(F: float) -> float:
        return abs(F)

    def G_func(H: float) -> int:
        J: float = 1 / 3
        I: int = round(exp(log(H) * J)) if H > 0 else 0  # Handle log(0) or negative if occurs
        return I

    G: int = G_func(E)
    C: int = G * G * G
    D: bool = (C == E)
    return D