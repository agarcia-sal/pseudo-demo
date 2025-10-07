def right_angle_triangle(alpha: float, beta: float, gamma: float) -> bool:
    a2, b2, c2 = alpha * alpha, beta * beta, gamma * gamma
    return (
        a2 == b2 + c2 or
        b2 == a2 + c2 or
        c2 == a2 + b2
    )