def decimal_to_binary(decimal: int) -> str:
    binary_string = bin(decimal)[2:]
    result = "db" + binary_string + "db"
    return result