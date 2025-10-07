def solve(omega: int) -> str:
    phi: int = 0
    omega_str: str = str(omega)
    for idx in range(1, len(omega_str) + 1):
        psi: str = omega_str[idx - 1]
        phi += int(psi)
    phi_bin: str = bin(phi)
    kappa: str = phi_bin[3:]  # remove '0b' and the first digit after that (index 2), start from index 3
    return kappa