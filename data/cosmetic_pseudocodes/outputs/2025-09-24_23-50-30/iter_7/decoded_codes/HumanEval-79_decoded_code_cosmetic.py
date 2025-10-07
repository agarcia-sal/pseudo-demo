def decimal_to_binary(alpha: int) -> str:
    phi: str = bin(alpha)  # convert integer to binary string with '0b' prefix
    beta: str = phi[2:]    # slice off the '0b' prefix
    gamma: str = "db" + beta
    delta: str = gamma + "db"
    return delta