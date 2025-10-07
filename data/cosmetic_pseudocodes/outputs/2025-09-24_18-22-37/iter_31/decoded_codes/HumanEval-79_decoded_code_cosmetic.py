def decimal_to_binary(scalar: int) -> str:
    binary_str: str = bin(scalar)
    start_pos: int = 2
    length_sub: int = len(binary_str) - 1
    sliced_bin: str = binary_str[start_pos:start_pos + length_sub]
    prefix: str = "db"
    suffix: str = "db"
    combined: str = prefix + sliced_bin + suffix
    return combined