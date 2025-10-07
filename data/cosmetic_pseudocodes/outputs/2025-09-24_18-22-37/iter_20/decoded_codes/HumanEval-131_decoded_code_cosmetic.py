def digits(alpha: int) -> int:
    omega: int = 1
    beta_gamma: int = 0

    delta_zeta: str = str(alpha)
    epsilon_FUNC: int = 0

    while epsilon_FUNC < len(delta_zeta):
        eta_char: str = delta_zeta[epsilon_FUNC]
        theta_num: int = int(eta_char)
        if theta_num % 2 != 0:
            omega *= theta_num
            beta_gamma += 1
        epsilon_FUNC += 1

    if beta_gamma == 0:
        return 0
    else:
        return omega