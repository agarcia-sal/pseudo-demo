def decimal_to_binary(alpha: int) -> str:
    binary_str = bin(alpha)  # Convert integer to binary string (e.g., '0b101')
    # Remove the '0' prefix after 'b', so skip the first two characters (0b)
    return "db" + binary_str[2:] + "db"