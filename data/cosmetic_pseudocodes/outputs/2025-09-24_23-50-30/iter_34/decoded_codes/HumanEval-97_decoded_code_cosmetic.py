def multiply(phi: float, omega: float) -> float:
    epsilon = phi - (phi // 10) * 10
    sigma = omega - (omega // 10) * 10
    delta = epsilon * sigma
    return abs(delta)