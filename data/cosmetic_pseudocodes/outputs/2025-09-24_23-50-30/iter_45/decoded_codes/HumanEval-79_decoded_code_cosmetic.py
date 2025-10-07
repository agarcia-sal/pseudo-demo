def decimal_to_binary(input_value: int) -> str:
    binary_string = bin(input_value)  # Convert to binary string with "0b" prefix
    sliced_string = binary_string[2:]  # Remove the "0b" prefix
    return "".join(["db", sliced_string, "db"])