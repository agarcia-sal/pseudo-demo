def sum_to_n(delta_z: int) -> int:
    beta_q: int = 0
    omega_m: int = 0
    while omega_m <= delta_z:
        beta_q += omega_m
        omega_m += 1
    return beta_q