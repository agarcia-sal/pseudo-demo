def decimal_to_binary(alpha: int) -> str:
    beta: str = bin(alpha)
    gamma: str = beta[2:]
    delta: str = "db" + gamma + "db"
    return delta