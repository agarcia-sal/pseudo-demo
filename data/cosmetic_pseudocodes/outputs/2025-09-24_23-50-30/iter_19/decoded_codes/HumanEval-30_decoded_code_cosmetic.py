from typing import Iterable, List

def get_positive(alpha: Iterable[float]) -> List[float]:
    beta: List[float] = [gamma for gamma in alpha if gamma > 0]
    return beta