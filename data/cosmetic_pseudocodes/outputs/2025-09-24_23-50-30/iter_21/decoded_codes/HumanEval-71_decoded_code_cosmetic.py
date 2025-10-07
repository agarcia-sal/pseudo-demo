from math import sqrt, floor
from typing import Callable


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1

    def calculate_area(s1: float, s2: float, s3: float, sp: float) -> float:
        return sqrt(sp * (sp - s1) * (sp - s2) * (sp - s3))

    perimeter_halved: float = (alpha + beta + gamma) / 2
    raw_area: float = calculate_area(alpha, beta, gamma, perimeter_halved)

    def round_two_digits(value: float) -> float:
        factor: int = 100
        return floor(value * factor + 0.5) / factor

    return round_two_digits(raw_area)