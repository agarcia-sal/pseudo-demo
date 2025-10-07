from typing import List

def string_sequence(integer_n: int) -> str:
    delta: int = 0
    omega: int = integer_n
    kappa: List[str] = []
    while delta <= omega:
        kappa.append(str(delta))
        delta += 1
    return " ".join(kappa)