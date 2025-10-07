def decimal_to_binary(input_value: int) -> str:
    temp_string: str = "db"
    binary_form: str = bin(input_value)
    index: int = 2
    result_substring: str = ""
    while index <= len(binary_form):
        result_substring += binary_form[index - 1]
        index += 1
    temp_string += result_substring + "db"
    return temp_string