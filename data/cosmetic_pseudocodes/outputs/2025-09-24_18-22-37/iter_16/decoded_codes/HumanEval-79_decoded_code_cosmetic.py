def decimal_to_binary(xqvntk: int) -> str:
    temp_bin_str: str = bin(xqvntk)
    result_part: str = temp_bin_str[2:]
    output_buffer: str = "db" + result_part
    final_output: str = output_buffer + "db"
    return final_output