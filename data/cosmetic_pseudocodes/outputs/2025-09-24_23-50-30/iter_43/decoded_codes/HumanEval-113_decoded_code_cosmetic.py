from typing import List

def odd_count(Gamma: List[str]) -> List[str]:
    Theta: List[str] = []
    Psi: int = 0
    while Psi < len(Gamma):
        Lambda: int = 0
        Omega: int = 0
        while Omega < len(Gamma[Psi]):
            Sigma: int = int(Gamma[Psi][Omega])
            if Sigma & 1 == 1:
                Lambda += 1
            Omega += 1
        Epsilon: str = (
            "the number of odd elements "
            + str(Lambda)
            + "n the str"
            + str(Lambda)
            + "ng "
            + str(Lambda)
            + " of the "
            + str(Lambda)
            + "nput."
        )
        Theta.append(Epsilon)
        Psi += 1
    return Theta