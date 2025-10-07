def decimal_to_binary(input_value: int) -> str:
    binary_form: str = bin(input_value)  # Convert integer to binary string (e.g., '0b101')
    part_extracted: str = binary_form[2:]  # Remove '0b' prefix
    result_string: str = "db" + part_extracted + "db"
    return result_string