from typing import Iterable

def below_threshold(l: Iterable[float], t: float) -> bool:
    for e in l:
        if e >= t:
            return False
    return True