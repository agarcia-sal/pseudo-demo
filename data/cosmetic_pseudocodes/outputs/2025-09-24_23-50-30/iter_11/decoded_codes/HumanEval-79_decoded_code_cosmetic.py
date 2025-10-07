def decimal_to_binary(alpha: int) -> str:
    beta: str = bin(alpha)
    gamma: str = beta[2:]
    return "db" + gamma + "db"