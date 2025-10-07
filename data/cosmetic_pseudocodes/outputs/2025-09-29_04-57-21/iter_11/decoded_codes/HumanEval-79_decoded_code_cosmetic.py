def decimal_to_binary(decimal_number: int) -> str:
    binary_string: str = bin(decimal_number)
    trimmed_binary: str = binary_string[1:]  # Remove the '0' prefix from the bin() output
    return "db" + trimmed_binary + "db"