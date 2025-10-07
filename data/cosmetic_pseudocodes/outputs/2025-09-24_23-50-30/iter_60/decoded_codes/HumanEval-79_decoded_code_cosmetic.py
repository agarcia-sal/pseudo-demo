def decimal_to_binary(alpha: int) -> str:
    # Convert alpha to binary string, removing the '0' prefix, then enclosing with "db"
    binary_str = bin(alpha)[2:]
    return f"db{binary_str}db"