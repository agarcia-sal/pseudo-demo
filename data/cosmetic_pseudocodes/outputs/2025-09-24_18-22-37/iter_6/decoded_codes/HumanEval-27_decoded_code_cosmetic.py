def flip_case(string_param: str) -> str:
    result_string = ""
    index_counter = 1
    while index_counter <= len(string_param):
        current_char = string_param[index_counter - 1]
        if 'a' <= current_char <= 'z':
            modified_char = current_char.upper()
        elif 'A' <= current_char <= 'Z':
            modified_char = current_char.lower()
        else:
            modified_char = current_char
        result_string += modified_char
        index_counter += 1
    return result_string