from typing import List

def derivative(kappa: List[int]) -> List[int]:
    psi: List[int] = []
    for theta in range(1, len(kappa)):
        psi.append(kappa[theta] * theta)
    return psi