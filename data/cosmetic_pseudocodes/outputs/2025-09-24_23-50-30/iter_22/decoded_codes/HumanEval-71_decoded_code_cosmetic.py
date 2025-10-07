from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not ((alpha + beta > gamma) and (alpha + gamma > beta) and (beta + gamma > alpha)):
        return -1.0
    p: float = (alpha + beta + gamma) * 0.5
    raw_area: float = (p * (p - alpha) * (p - beta) * (p - gamma)) ** 0.5
    precise_area: float = round(raw_area * 100) / 100
    return precise_area