def is_happy(input_str: str) -> bool:
    if len(input_str) < 3:
        return False
    for pos in range(len(input_str) - 2):
        # Check that all three consecutive chars are distinct
        if not (input_str[pos] != input_str[pos + 1] and input_str[pos + 1] != input_str[pos + 2] and input_str[pos] != input_str[pos + 2]):
            return False
    return True