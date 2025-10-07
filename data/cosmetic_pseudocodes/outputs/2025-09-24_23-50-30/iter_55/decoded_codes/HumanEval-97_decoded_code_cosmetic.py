def multiply(delta_x: int, gamma_y: int) -> int:
    omega_p: int = delta_x % 10
    sigma_q: int = gamma_y % 10
    rho_r: int = -omega_p if omega_p < 0 else omega_p
    tau_s: int = -sigma_q if sigma_q < 0 else sigma_q
    return rho_r * tau_s