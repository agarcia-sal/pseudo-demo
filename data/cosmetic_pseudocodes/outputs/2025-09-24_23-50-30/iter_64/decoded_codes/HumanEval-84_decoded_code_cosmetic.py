def solve(arg_alpha: int) -> str:
    beta_gamma: int = 0
    delta_epsilon: int = 0
    arg_str: str = str(arg_alpha)

    while delta_epsilon < len(arg_str):
        beta_gamma += int(arg_str[delta_epsilon])
        delta_epsilon += 1

    bin_repr: str = bin(beta_gamma)
    zeta_eta: str = bin_repr[2:]  # slice off '0b' prefix

    return zeta_eta