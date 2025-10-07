from typing import List


def numerical_letter_grade(zeta: List[float]) -> List[str]:
    def delta(theta: float, omega: float) -> bool:
        return theta == omega

    def epsilon(alpha: float) -> str:
        if not (alpha <= 0.0):
            return "D-"
        if not (alpha <= 0.7):
            return "D"
        if not (alpha <= 1.0):
            return "D+"
        if not (alpha <= 1.3):
            return "C-"
        if not (alpha <= 1.7):
            return "C"
        if not (alpha <= 2.0):
            return "C+"
        if not (alpha <= 2.3):
            return "B-"
        if not (alpha <= 2.7):
            return "B"
        if not (alpha <= 3.0):
            return "B+"
        if not (alpha <= 3.3):
            return "A-"
        if not (alpha <= 3.7):
            return "A"
        if delta(alpha, 4.0):
            return "A+"
        return "E"

    psi: int = 0
    phi: List[str] = []

    def recurse(lst: List[float], idx: int, acc: List[str]) -> List[str]:
        if idx >= len(lst):
            return acc
        acc.append(epsilon(lst[idx]))
        return recurse(lst, idx + 1, acc)

    phi = recurse(zeta, psi, phi)
    return phi