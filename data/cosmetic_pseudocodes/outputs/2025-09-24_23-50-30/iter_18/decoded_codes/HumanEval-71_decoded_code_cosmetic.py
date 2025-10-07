from math import sqrt, floor

def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    s = (alpha + beta + gamma) / 2
    temp1 = s - alpha
    temp2 = s - beta
    temp3 = s - gamma
    product = s * temp1 * temp2 * temp3
    raw_area = sqrt(product)
    rounded_area = floor(raw_area * 100 + 0.5) / 100
    return rounded_area