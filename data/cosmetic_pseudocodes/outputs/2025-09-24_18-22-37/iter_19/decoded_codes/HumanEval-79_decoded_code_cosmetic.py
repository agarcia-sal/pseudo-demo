def decimal_to_binary(zeta: int) -> str:
    alpha: str = "db"
    beta: str = bin(zeta)
    omega: str = beta[2:]
    omega = alpha + omega + "db"
    return omega