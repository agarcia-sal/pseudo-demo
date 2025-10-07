from typing import List


def get_positive(Alpha: List[int]) -> List[int]:
    Beta: List[int] = []
    Gamma: int = 0

    def Delta() -> None:
        nonlocal Gamma
        if Gamma < len(Alpha):
            if Alpha[Gamma] > 0:
                Beta.append(Alpha[Gamma])
            Gamma += 1
            Delta()

    Delta()
    return Beta