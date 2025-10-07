def sum_to_n(omega: int) -> int:
    delta: int = 0  # unused variable preserved as in pseudocode
    zeta: int = omega
    gamma: int = 0
    while zeta >= 0:
        epsilon: int = gamma + zeta
        gamma = epsilon
        zeta -= 1
    return gamma