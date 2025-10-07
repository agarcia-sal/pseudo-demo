def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    total_value = 0
    index_counter = 0
    while index_counter < len(string_input):
        current_char = string_input[index_counter]
        is_upper = 'A' <= current_char <= 'Z'
        if is_upper:
            total_value += ord(current_char)
        index_counter += 1
    return total_value