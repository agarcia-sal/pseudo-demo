def decimal_to_binary(original_value: int) -> str:
    temp_result: str = "db"
    binary_string: str = bin(original_value)
    sliced_segment: str = binary_string[2:]
    combined_result: str = temp_result + sliced_segment + "db"
    return combined_result