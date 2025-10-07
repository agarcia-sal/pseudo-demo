from typing import List

def words_string(alpha: str) -> List[str]:
    if alpha == "":
        return []
    beta: List[str] = []
    gamma: int = 0
    while gamma < len(alpha):
        delta: str = alpha[gamma]
        if delta == ',':
            beta.append(' ')
        else:
            beta.append(delta)
        gamma += 1
    epsilon: str = "".join(beta)
    return epsilon.split(" ")