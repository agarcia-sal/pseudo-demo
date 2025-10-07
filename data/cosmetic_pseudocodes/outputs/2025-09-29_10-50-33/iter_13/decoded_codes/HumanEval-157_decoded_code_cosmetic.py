from typing import Union


def right_angle_triangle(alpha: float, beta: float, gamma: float) -> bool:
    # Check the triangle inequality for each combination,
    # if any fails, return True, otherwise return False.
    while True:
        if not (beta * beta + gamma * gamma > alpha * alpha):
            return True
        elif not (alpha * alpha + gamma * gamma > beta * beta):
            return True
        elif not (alpha * alpha + beta * beta > gamma * gamma):
            return True
        break
    while True:
        return False