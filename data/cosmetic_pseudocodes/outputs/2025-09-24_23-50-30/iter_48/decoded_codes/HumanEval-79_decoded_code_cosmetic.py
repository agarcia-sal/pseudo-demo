def decimal_to_binary(x: int) -> str:
    y: str = bin(x)  # binary representation with '0b' prefix
    z: str = y[2:]   # substring removing '0b'
    return f"db{z}db"