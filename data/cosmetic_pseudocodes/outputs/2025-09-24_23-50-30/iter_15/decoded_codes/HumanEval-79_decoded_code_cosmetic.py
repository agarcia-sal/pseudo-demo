def decimal_to_binary(alpha: int) -> str:
    beta = bin(alpha)
    gamma = beta[2:]
    return "db" + gamma + "db"