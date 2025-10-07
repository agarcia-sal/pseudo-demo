def decimal_to_binary(gamma: int) -> str:
    omega: str = bin(gamma)
    alpha: str = omega[2:]
    beta: str = "db" + alpha + "db"
    return beta