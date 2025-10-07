def prime_length(input_string: str) -> bool:
    string_len: int = len(input_string)
    if string_len <= 1:
        return False
    counter_variable: int = 2
    while counter_variable < string_len:
        remainder_check: int = string_len - (string_len // counter_variable) * counter_variable
        if remainder_check == 0:
            return False
        counter_variable += 1
    return True