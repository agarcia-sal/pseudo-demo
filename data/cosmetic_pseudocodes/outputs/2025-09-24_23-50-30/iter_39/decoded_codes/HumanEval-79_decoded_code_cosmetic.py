def decimal_to_binary(alpha: int) -> str:
    beta: str = bin(alpha)
    return "db" + beta[2:] + "db"