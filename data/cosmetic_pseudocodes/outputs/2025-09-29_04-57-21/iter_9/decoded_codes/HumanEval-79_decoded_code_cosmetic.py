def decimal_to_binary(decimal_number: int) -> str:
    binary_string = bin(decimal_number)  # e.g. '0b101'
    trimmed_binary = binary_string[2:]  # remove '0b' prefix
    return "db" + trimmed_binary + "db"