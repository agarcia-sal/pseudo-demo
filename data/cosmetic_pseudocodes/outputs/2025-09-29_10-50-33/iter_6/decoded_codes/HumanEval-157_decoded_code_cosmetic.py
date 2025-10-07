from typing import Union


def right_angle_triangle(alpha: Union[int, float], beta: Union[int, float], gamma: Union[int, float]) -> bool:
    a2 = alpha * alpha
    b2 = beta * beta
    c2 = gamma * gamma
    return a2 == b2 + c2 or b2 == a2 + c2 or c2 == a2 + b2