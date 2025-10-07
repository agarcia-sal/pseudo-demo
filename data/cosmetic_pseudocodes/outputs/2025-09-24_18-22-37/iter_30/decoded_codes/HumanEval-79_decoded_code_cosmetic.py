def decimal_to_binary(alpha: int) -> str:
    temp_bin: str = bin(alpha)
    temp_str: str = temp_bin[2:]
    result: str = "db" + temp_str + "db"
    return result