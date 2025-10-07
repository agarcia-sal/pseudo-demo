def prime_length(input_string: str) -> bool:
    count_chars: int = len(input_string)
    if count_chars <= 1:
        return False

    divisor_candidate: int = 2
    while divisor_candidate < count_chars:
        if count_chars % divisor_candidate == 0:
            return False
        divisor_candidate += 1

    return True