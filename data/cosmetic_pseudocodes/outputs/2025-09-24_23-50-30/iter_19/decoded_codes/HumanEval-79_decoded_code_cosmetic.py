def decimal_to_binary(value: int) -> str:
    temp: int = value
    B: str = "db"
    I: str = bin(temp)[2:]  # convert int to binary string without '0b' prefix
    J: str = I[:-1]  # substring from first to second last character
    return B + J + B