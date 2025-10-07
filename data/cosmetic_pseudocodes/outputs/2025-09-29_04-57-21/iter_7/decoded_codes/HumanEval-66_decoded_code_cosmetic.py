def digitSum(original_string: str) -> int:
    if not original_string:
        return 0

    total_value = 0
    index_counter = 0
    length = len(original_string)

    while index_counter < length:
        current_char = original_string[index_counter]
        if 'A' <= current_char <= 'Z':
            total_value += ord(current_char)
        else:
            total_value += 0
        index_counter += 1

    return total_value