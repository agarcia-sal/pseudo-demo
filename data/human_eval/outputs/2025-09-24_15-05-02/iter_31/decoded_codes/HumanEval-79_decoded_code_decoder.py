def decimal_to_binary(decimal_number: int) -> str:
    return f"db{bin(decimal_number)[2:]}db"