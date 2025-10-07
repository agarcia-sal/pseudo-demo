def decimal_to_binary(num_decimal: int) -> str:
    binary_string = bin(num_decimal)
    result_string = "db" + binary_string[2:] + "db"
    return result_string