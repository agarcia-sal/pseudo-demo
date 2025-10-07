def decimal_to_binary(decimal_number: int) -> str:
    binary_string: str = bin(decimal_number)
    sliced_part: str = binary_string[2:]
    return f"db{sliced_part}db"