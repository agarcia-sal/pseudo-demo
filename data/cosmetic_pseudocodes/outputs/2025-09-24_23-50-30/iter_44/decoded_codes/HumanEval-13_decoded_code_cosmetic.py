from math import floor

def greatest_common_divisor(alpha: int, beta: int) -> int:
    gamma = alpha
    delta = beta
    while delta != 0:
        epsilon = delta
        delta = gamma - floor(gamma / delta) * delta
        gamma = epsilon
    return gamma