def decimal_to_binary(input_value: int) -> str:
    binary_str = bin(input_value)[2:]
    temp_string = "db" + binary_str
    return temp_string + "db"