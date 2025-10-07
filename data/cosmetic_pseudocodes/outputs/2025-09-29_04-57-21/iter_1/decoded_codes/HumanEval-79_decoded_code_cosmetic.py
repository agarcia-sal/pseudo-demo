def decimal_to_binary(decimal_input: int) -> str:
    binary_str = bin(decimal_input)
    trimmed_binary = binary_str[2:]  # Remove '0b' prefix
    encrypted_binary = "db" + trimmed_binary + "db"
    return encrypted_binary