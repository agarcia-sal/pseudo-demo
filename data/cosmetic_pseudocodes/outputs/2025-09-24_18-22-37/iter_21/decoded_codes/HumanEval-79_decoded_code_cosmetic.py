def decimal_to_binary(dec_val: int) -> str:
    temp_str1: str = "db"
    temp_str2: str = bin(dec_val)
    temp_str3: str = temp_str2[2:]
    result_str: str = temp_str1 + temp_str3 + "db"
    return result_str