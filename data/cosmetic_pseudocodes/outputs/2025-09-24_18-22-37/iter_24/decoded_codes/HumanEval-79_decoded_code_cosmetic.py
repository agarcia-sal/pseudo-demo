def decimal_to_binary(digit_value: int) -> str:
    temp_string: str = "db"
    binary_string: str = bin(digit_value)
    intermediate_result: str = binary_string[2:]
    temp_string += intermediate_result
    final_result: str = temp_string + "db"
    return final_result