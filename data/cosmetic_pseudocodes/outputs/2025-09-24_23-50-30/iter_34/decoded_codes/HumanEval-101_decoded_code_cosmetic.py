from typing import List

def words_string(delta: str) -> List[str]:
    if delta == "":
        return []
    else:
        omega: List[str] = []
        mu: int = 0
        while mu < len(delta):
            psi: str = delta[mu]
            if psi == ",":
                omega.append(" ")
            else:
                omega.append(psi)
            mu += 1
        tau: str = "".join(omega)
        return tau.split()