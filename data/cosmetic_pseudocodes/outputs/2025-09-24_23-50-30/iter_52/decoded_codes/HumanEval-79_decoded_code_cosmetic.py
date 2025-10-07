def decimal_to_binary(parameter_one: int) -> str:
    binary_str = bin(parameter_one)[2:]  # convert to binary and remove '0b'
    return f"db{binary_str}db"