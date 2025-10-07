from typing import List

def anti_shuffle(zeta: str) -> str:
    omega: List[str] = zeta.split(" ")

    def Psi(index: int, alpha: List[str]) -> List[str]:
        if index == len(omega):
            return alpha
        beta: str = "".join(sorted(list(omega[index])))
        return Psi(index + 1, alpha + [beta])

    Gamma: List[str] = Psi(0, [])
    return " ".join(Gamma)