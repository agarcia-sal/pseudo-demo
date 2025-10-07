from math import sqrt, floor

def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if gamma >= alpha + beta or beta >= alpha + gamma or alpha >= beta + gamma:
        return -1
    p = (alpha + beta + gamma) * 0.5
    product = p * (p - alpha) * (p - beta) * (p - gamma)
    root = sqrt(product)
    final = floor(root * 100 + 0.5) / 100
    return final