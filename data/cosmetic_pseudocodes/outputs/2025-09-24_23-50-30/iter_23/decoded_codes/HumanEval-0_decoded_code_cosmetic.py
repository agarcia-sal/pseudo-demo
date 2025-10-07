from typing import Sequence

def has_close_elements(array_alpha: Sequence[float], epsilon: float) -> bool:
    length = len(array_alpha)
    for i in range(length):
        for j in range(length):
            if i != j and abs(array_alpha[i] - array_alpha[j]) < epsilon:
                return True
    return False