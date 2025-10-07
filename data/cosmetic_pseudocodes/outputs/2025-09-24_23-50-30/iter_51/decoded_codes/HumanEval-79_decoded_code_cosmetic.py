def decimal_to_binary(alpha: int) -> str:
    binary_str = bin(alpha)  # e.g. '0b1010'
    # Extract substring starting at index 2 to end
    # which excludes '0b' prefix
    return "db" + binary_str[2:] + "db"