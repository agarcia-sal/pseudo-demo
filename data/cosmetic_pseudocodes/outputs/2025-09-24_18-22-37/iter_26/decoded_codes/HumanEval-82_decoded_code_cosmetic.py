def prime_length(input_string: str) -> bool:
    total_chars = len(input_string)
    if total_chars in (0, 1):
        return False

    divisor_candidate = 2
    while divisor_candidate < total_chars:
        if total_chars % divisor_candidate == 0:
            return False
        divisor_candidate += 1

    return True