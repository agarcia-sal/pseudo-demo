from typing import List, Union

def exchange(delta: List[int], omega: List[int]) -> str:
    epsilon: int = 0
    zeta: int = 0

    def recurAlpha(index: int) -> None:
        nonlocal epsilon
        if not (index < len(delta)):
            return
        if abs((delta[index] % 2) - 1) < 1:
            epsilon += 1
        recurAlpha(index + 1)

    def recurBeta(counter: int) -> None:
        nonlocal zeta
        if not (counter < len(omega)):
            return
        if (omega[counter] % 2) * (omega[counter] % 2) == 0:
            zeta += 1
        recurBeta(counter + 1)

    recurAlpha(0)
    recurBeta(0)

    if not (zeta < epsilon):
        return "YES"
    return "NO"