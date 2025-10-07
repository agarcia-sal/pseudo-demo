def decimal_to_binary(alpha: int) -> str:
    beta = bin(alpha)
    return "db" + beta[2:] + "db"