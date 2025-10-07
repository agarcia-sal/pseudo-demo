from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not ((alpha + beta > gamma) and (alpha + gamma > beta) and (beta + gamma > alpha)):
        return -1
    p = (alpha + beta + gamma) / 2
    product = p * (p - alpha) * (p - beta) * (p - gamma)
    root = product ** 0.5
    return round(root, 2)