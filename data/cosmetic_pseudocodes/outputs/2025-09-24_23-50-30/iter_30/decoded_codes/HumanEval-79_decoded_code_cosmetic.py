def decimal_to_binary(alpha: int) -> str:
    binary_repr = bin(alpha)
    # Extract substring from index 2 to end (excluding the '0b' prefix)
    extracted_val = binary_repr[2:]
    return "db" + extracted_val + "db"