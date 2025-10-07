def decimal_to_binary(aux_decimal: int) -> str:
    db_prefix = "db"
    binary_repr = bin(aux_decimal)  # includes '0b' prefix
    temp_substr = binary_repr[2:]   # substring removing '0b'
    result_str = db_prefix + temp_substr + db_prefix
    return result_str