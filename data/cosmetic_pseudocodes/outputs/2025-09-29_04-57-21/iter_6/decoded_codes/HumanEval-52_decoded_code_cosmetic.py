from typing import Sequence

def below_threshold(sequence: Sequence[float], limit: float) -> bool:
    index: int = 0
    while index < len(sequence):
        value = sequence[index]
        if not (value < limit):
            return False
        index += 1
    return True