def is_happy(text_param: str) -> bool:
    if len(text_param) < 3:
        return False
    for loop_counter in range(len(text_param) - 2):
        first_char = text_param[loop_counter]
        second_char = text_param[loop_counter + 1]
        third_char = text_param[loop_counter + 2]
        # Check all three characters are distinct
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False
    return True