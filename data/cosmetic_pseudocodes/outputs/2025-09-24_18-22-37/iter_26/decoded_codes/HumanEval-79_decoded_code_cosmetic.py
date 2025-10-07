def decimal_to_binary(kappa: int) -> str:
    temp_string: str = "db"
    binary_repr: str = bin(kappa)
    slice_start_index: int = 2
    binary_substring: str = binary_repr[slice_start_index:]
    temp_string += binary_substring
    final_result: str = temp_string + "db"
    return final_result