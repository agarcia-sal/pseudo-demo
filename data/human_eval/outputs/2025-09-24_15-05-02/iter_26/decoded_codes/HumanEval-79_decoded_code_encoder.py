def decimal_to_binary(decimal: int) -> str:
    return "db" + bin(decimal)[2:] + "db"