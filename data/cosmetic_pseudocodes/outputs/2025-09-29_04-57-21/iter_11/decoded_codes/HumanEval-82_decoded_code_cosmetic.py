def prime_length(input_string: str) -> bool:
    string_scale: int = len(input_string)
    if string_scale <= 1:
        return False
    divisor_candidate: int = 2
    while divisor_candidate < string_scale:
        if string_scale % divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True