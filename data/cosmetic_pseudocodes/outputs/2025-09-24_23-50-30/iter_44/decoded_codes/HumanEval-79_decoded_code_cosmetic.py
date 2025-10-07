def decimal_to_binary(number_decimal: int) -> str:
    prefix = "db"
    binary_str = bin(number_decimal)
    binary_substring = binary_str[2:]
    suffix = "db"
    return prefix + binary_substring + suffix