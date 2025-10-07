from typing import Literal

def right_angle_triangle(alpha: float, beta: float, gamma: float) -> Literal[bool]:
    # Check if any side squared is greater than the sum of the squares of the other two sides
    if not (alpha * alpha > beta * beta + gamma * gamma) and \
       not (beta * beta > alpha * alpha + gamma * gamma) and \
       not (gamma * gamma > alpha * alpha + beta * beta):
        return True
    return False