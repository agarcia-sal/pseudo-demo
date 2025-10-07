def decimal_to_binary(x: int) -> str:
    y = bin(x)[2:]
    return f"db{y}db"