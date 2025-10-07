def multiply(delta_x: int, theta_y: int) -> int:
    phi_m: int = delta_x % 10
    if phi_m < 0:
        phi_m = -phi_m
    omega_n: int = theta_y % 10
    if omega_n < 0:
        omega_n = -omega_n
    chi_p: int = phi_m
    chi_p = chi_p * omega_n
    return chi_p