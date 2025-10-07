def decimal_to_binary(decimal: int) -> str:
    binary_string = bin(decimal)
    trimmed_binary = binary_string[2:]
    result_string = "db" + trimmed_binary + "db"
    return result_string