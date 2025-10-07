def decimal_to_binary(delta: int) -> str:
    omega = "db" + bin(delta)[2:] + "db"
    return omega