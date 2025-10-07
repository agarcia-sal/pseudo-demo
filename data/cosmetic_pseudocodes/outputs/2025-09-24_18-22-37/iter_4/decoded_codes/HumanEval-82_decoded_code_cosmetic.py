def prime_length(input_string: str) -> bool:
    string_len: int = len(input_string)
    if string_len in (0, 1):
        return False
    divisor_candidate: int = 2
    while divisor_candidate < string_len:
        if string_len % divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True