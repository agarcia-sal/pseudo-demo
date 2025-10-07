from typing import List

def flip_case(delta: str) -> str:
    omega: List[str] = []
    for theta in range(len(delta)):
        kappa: str = delta[theta]
        if 'a' <= kappa <= 'z':
            omega.append(kappa.upper())
        elif 'A' <= kappa <= 'Z':
            omega.append(kappa.lower())
        else:
            omega.append(kappa)
    return "".join(omega)