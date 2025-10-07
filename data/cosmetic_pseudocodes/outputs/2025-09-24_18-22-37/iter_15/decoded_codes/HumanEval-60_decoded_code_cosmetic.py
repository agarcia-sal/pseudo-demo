def sum_to_n(alpha_k: int) -> int:
    beta_m: int = 0
    gamma_z: int = 0
    while gamma_z <= alpha_k:
        delta_y: int = gamma_z + beta_m
        beta_m = delta_y
        gamma_z += 1
    return beta_m