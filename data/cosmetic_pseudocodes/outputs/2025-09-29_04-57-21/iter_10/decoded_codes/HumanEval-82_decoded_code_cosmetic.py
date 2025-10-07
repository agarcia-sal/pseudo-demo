def prime_length(input_string: str) -> bool:
    total_chars: int = len(input_string)
    if total_chars <= 1:
        return False

    candidate_divisor: int = 2
    while candidate_divisor < total_chars:
        if total_chars % candidate_divisor == 0:
            return False
        candidate_divisor += 1

    return True