from typing import Sequence, List

def derivative(alpha: Sequence[float]) -> List[float]:
    return [alpha[gamma] * gamma for gamma in range(1, len(alpha))]