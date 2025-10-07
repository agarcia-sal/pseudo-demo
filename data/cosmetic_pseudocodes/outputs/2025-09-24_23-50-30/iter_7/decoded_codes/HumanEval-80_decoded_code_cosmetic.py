def is_happy(string_input: str) -> bool:
    integer_len = len(string_input)
    if integer_len < 3:  # equivalent to (integer_len - 3) < 0
        return False
    for integer_position in range(integer_len - 2):
        ch_a = string_input[integer_position]
        ch_b = string_input[integer_position + 1]
        ch_c = string_input[integer_position + 2]
        # If any two are equal, return False
        if not (ch_a != ch_b and ch_b != ch_c and ch_a != ch_c):
            return False
    return True