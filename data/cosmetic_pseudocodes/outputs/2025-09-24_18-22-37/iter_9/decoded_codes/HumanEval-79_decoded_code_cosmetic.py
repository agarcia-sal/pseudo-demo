def decimal_to_binary(input_value: int) -> str:
    binary_string: str = bin(input_value)
    first_trimmed_part: str = binary_string[2:]
    return "db" + first_trimmed_part + "db"