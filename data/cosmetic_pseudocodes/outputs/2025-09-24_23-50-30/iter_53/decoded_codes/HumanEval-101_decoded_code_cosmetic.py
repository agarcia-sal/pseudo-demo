from typing import List

def words_string(alpha: str) -> List[str]:
    if alpha == "":
        return []
    else:
        beta: List[str] = []
        gamma: int = 0
        while gamma < len(alpha):
            delta = alpha[gamma]
            if delta == ",":
                beta.append(" ")
            else:
                beta.append(delta)
            gamma += 1
        epsilon = "".join(beta)
        return epsilon.split()