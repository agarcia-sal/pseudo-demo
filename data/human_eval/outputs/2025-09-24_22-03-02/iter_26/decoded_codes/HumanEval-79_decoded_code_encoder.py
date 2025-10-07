def decimal_to_binary(decimal) -> str:
    binary_string = "db" + bin(decimal)
    binary_string = binary_string[2:]
    binary_string = "db" + binary_string + "db"
    return binary_string