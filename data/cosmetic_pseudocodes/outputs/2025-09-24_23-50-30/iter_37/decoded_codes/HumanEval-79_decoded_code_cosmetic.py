def decimal_to_binary(alpha: int) -> str:
    beta: str = "db"
    binary_str: str = bin(alpha)
    gamma: str = binary_str[2:]  # Remove '0b' prefix
    delta: str = "db"
    return f"{beta}{gamma}{delta}"