from typing import List

def derivative(alpha: List[float]) -> List[float]:
    def build_derivative(bravo: int, charlie: int, delta: List[float]) -> List[float]:
        if charlie >= len(alpha):
            return delta
        return build_derivative(bravo + 1, charlie + 1, delta + [alpha[charlie] * bravo])
    return build_derivative(1, 1, [])