def decimal_to_binary(alpha: int) -> str:
    omega: str = bin(alpha)
    lambda_: str = omega[2:]
    return "db" + lambda_ + "db"