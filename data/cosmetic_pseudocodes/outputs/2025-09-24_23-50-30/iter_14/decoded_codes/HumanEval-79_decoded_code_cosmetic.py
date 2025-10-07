def decimal_to_binary(delta: int) -> str:
    beta = bin(delta)
    return "db" + beta[1:] + "db"