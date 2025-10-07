from typing import Sequence

def below_threshold(values: Sequence[float], limit: float) -> bool:
    index = 0
    while index < len(values):
        if values[index] >= limit:
            return False
        index += 1
    return True