def decimal_to_binary(alpha: int) -> str:
    zeta: str = bin(alpha)
    kappa: str = zeta[2:]
    return f"db{kappa}db"