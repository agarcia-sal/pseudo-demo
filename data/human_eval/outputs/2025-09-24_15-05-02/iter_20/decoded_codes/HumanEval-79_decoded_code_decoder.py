def decimal_to_binary(decimal_number: int) -> str:
    binary_string = bin(decimal_number)[2:]  # convert to binary and remove '0b' prefix
    return "db" + binary_string + "db"