def multiply(alpha_x: int, beta_y: int) -> int:
    gamma_p: int = alpha_x % 10
    if gamma_p < 0:
        gamma_p = -gamma_p

    delta_q: int = beta_y % 10
    if delta_q < 0:
        delta_q = -delta_q

    epsilon_r: int = gamma_p * delta_q

    return epsilon_r