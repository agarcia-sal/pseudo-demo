def decimal_to_binary(numeric_value: int) -> str:
    binary_str = bin(numeric_value)[2:]  # strip '0b' prefix
    output_string = "db"
    idx = 1
    while idx < len(binary_str):
        output_string += binary_str[idx]
        idx += 1
    output_string += "db"
    return output_string