def decimal_to_binary(omega: int) -> str:
    alpha: str = bin(omega)
    beta: str = alpha[2:]
    return "db" + beta + "db"