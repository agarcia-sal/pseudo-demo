def decimal_to_binary(input_value: int) -> str:
    temp_string: str = bin(input_value)
    new_string: str = "db" + temp_string[2:] + "db"
    return new_string