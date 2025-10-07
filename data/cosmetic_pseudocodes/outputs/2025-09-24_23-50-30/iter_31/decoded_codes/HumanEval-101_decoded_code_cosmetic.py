from typing import List

def words_string(psi: str) -> List[str]:
    if psi == "":
        return []
    else:
        alpha: List[str] = []
        beta: int = 0
        while beta < len(psi):
            gamma: str = psi[beta]
            if gamma == ",":
                alpha.append(" ")
            else:
                alpha.append(gamma)
            beta += 1
        delta: str = "".join(alpha)
        return delta.split(" ")