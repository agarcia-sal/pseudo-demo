def digitSum(text_param: str) -> int:
    if text_param == "":
        return 0
    total_value: int = 0
    index_counter: int = 1
    text_length: int = len(text_param)
    while index_counter <= text_length:
        current_char: str = text_param[index_counter - 1]
        if "A" <= current_char <= "Z":
            total_value += ord(current_char)
        index_counter += 1
    return total_value