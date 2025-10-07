def digits(z: int) -> int:
    kappa: int = 1
    rho: int = 0
    gamma: int = 0
    z_str: str = str(z)
    while gamma < len(z_str):
        chi: str = z_str[gamma]
        psi: int = int(chi)
        if psi % 2 != 0:
            kappa *= psi
            rho += 1
        gamma += 1
    if rho == 0:
        return 0
    return kappa