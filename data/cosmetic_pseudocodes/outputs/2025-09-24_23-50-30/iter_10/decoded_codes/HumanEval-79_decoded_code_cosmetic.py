def decimal_to_binary(apparent_value: int) -> str:
    bit_string = bin(apparent_value)
    truncated_bits = bit_string[2:]
    return "db" + truncated_bits + "db"