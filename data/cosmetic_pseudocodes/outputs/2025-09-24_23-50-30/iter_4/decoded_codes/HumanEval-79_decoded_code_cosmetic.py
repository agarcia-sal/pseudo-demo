def decimal_to_binary(decimal_number: int) -> str:
    binary_str = bin(decimal_number)  # Convert to binary string with '0b' prefix
    trimmed_binary = binary_str[2:]   # Remove '0b' prefix
    result = "db" + trimmed_binary + "db"
    return result