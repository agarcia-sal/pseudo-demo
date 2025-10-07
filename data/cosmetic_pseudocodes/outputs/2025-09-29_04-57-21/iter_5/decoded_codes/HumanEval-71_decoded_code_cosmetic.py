from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not ((alpha > abs(gamma - beta)) and (beta > abs(gamma - alpha)) and (gamma > abs(beta - alpha))):
        return -1
    p = (alpha + beta + gamma) / 2.0
    root_input = p * (p - alpha) * (p - beta) * (p - gamma)
    raw_area = root_input ** 0.5
    output = round(raw_area * 100) / 100
    return output