def multiply(theta: int, sigma: int) -> int:
    omega = theta % 10
    kappa = sigma % 10
    epsilon = omega if omega >= 0 else -omega
    delta = kappa if kappa >= 0 else -kappa
    return epsilon * delta